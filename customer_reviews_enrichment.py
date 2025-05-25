import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyodbc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Define a function to fetch data from a SQL database using a SQL query
def fetch_data_from_sql():
    # Define the connection string with parameters for the database connection
    conn_str = (
        "Driver={SQL Server};"
        "Server=DESKTOP-QPEBF35\\SQLEXPRESS;"
        "Database=MarketingAnalytics;"
        "Trusted_Connection=yes;"
    )

    from sqlalchemy import create_engine

    engine = create_engine(
    "mssql+pyodbc://DESKTOP-QPEBF35\\SQLEXPRESS/MarketingAnalytics?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )


    # Define the SQL query to fetch customer reviews data
    query = "SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, ReviewText FROM dbo.customer_reviews"

    # Execute the query using the SQLAlchemy engine
    df = pd.read_sql(query, engine)

    return df

customer_reviews_df = fetch_data_from_sql()

# Initialize the VADER sentiment intensity analyzer for analyzing the sentiment of text data
sia = SentimentIntensityAnalyzer()

# Define a function to calculate sentiment scores using VADER
def calculate_sentiment(review):
    sentiment = sia.polarity_scores(review)
    return sentiment['compound']

# Define a function to categorize sentiment using both the sentiment score and the review rating
def categorize_sentiment(score, rating):
    # Use both the text sentiment score and the numerical rating to determine sentiment category
    if score > 0.05:
        if rating >= 4:
            return 'Positive'
        elif rating == 3:
            return 'Mixed Positive'
        else:
            return 'Mixed Negative'
    elif score < -0.05:
        if rating <= 2:
            return 'Negative'
        elif rating == 3:
            return 'Mixed Negative'
        else:
            return 'Mixed Positive'
    else:  # Neutral sentiment score
        if rating >= 4:
            return 'Positive'
        elif rating <= 2:
            return 'Negative'
        else:
            return 'Neutral'

# Define a function to bucket sentiment scores into text ranges
def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0'
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'
    else:
        return '-1.0 to -0.5'

# Apply sentiment analysis to calculate sentiment scores for each review
customer_reviews_df['SentimentScore'] = customer_reviews_df['ReviewText'].apply(calculate_sentiment)

# Apply sentiment categorization using both text and rating
customer_reviews_df['SentimentCategory'] = customer_reviews_df.apply(
    lambda row: categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1)

# Apply sentiment bucketing to categorize scores into defined ranges
customer_reviews_df['SentimentBucket'] = customer_reviews_df['SentimentScore'].apply(sentiment_bucket)

# Display the first few rows of the DataFrame with sentiment scores, categories, and buckets
print(customer_reviews_df.head())

# Save the DataFrame with sentiment scores, categories, and buckets to a new CSV file
customer_reviews_df.to_csv('fact_customer_reviews_with_sentiment.csv', index=False)

# Visualization for Sentiment score and distribution
sns.histplot(customer_reviews_df['SentimentScore'], bins=30, kde=True)
plt.title('Sentiment Score Distribution')
plt.show()

#Visualization for Outliers in Sentiment Score and Ratings
sns.set(style="whitegrid")

plt.figure(figsize=(8, 6))
sns.boxplot(y=customer_reviews_df['SentimentScore'], color='skyblue')

plt.title('Box Plot of Sentiment Scores', fontsize=14)
plt.ylabel('Sentiment Score')

plt.tight_layout()
plt.show()

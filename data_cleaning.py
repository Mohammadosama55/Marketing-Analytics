import pandas as pd
import numpy as np
from textblob import TextBlob  # For sentiment analysis (if not already done)

def load_data():
    # Load the raw customer reviews data
    df = pd.read_csv("fact_customer_reviews_with_sentiment.csv")
    return df

def clean_data(df):
    # Handle missing values
    df['review_text'] = df['review_text'].fillna("No review")
    df['rating'] = df['rating'].fillna(df['rating'].median())

    # Remove duplicates
    df = df.drop_duplicates(subset=['customer_id', 'product_id', 'review_text'])

    # Feature engineering: Extract review length
    df['review_length'] = df['review_text'].apply(len)

    # Sentiment polarity (if not already in CSV)
    df['sentiment_polarity'] = df['review_text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

    # Outlier handling for ratings (IQR method)
    Q1 = df['rating'].quantile(0.25)
    Q3 = df['rating'].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df['rating'] < (Q1 - 1.5 * IQR)) | (df['rating'] > (Q3 + 1.5 * IQR))]

    return df

if __name__ == "__main__":
    df = load_data()
    cleaned_df = clean_data(df)
    cleaned_df.to_csv("cleaned_customer_reviews.csv", index=False)
    print("Data cleaned and saved to 'cleaned_customer_reviews.csv'")
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def generate_summary_statistics(df):
    """Generate comprehensive summary statistics for the dataset."""
    stats_dict = {
        'basic_stats': df.describe(),
        'missing_values': df.isnull().sum(),
        'unique_values': df.nunique(),
        'skewness': df.skew(numeric_only=True),
        'kurtosis': df.kurtosis(numeric_only=True)
    }
    
    # Correlation analysis
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    stats_dict['correlations'] = df[numeric_cols].corr()
    
    return stats_dict

def plot_rating_distribution(df, save_path="plots/rating_distribution.png"):
    """Plot the distribution of ratings with summary statistics."""
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='rating', bins=5, kde=True)
    plt.axvline(df['rating'].mean(), color='red', linestyle='--', label=f'Mean: {df["rating"].mean():.2f}')
    plt.axvline(df['rating'].median(), color='green', linestyle='--', label=f'Median: {df["rating"].median():.2f}')
    plt.title("Distribution of Customer Ratings")
    plt.legend()
    plt.savefig(save_path)
    plt.close()

def plot_sentiment_analysis(df, save_path="plots/sentiment_analysis.png"):
    """Create sentiment analysis visualizations."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Sentiment vs Rating
    sns.scatterplot(data=df, x='sentiment_polarity', y='rating', alpha=0.6, ax=ax1)
    ax1.set_title("Sentiment Polarity vs Rating")
    
    # Sentiment Distribution
    sns.histplot(data=df, x='sentiment_polarity', bins=30, kde=True, ax=ax2)
    ax2.set_title("Distribution of Sentiment Polarity")
    
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_review_length_analysis(df, save_path="plots/review_length_analysis.png"):
    """Analyze and visualize review length patterns."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Review Length Distribution
    sns.histplot(data=df, x='review_length', bins=30, kde=True, ax=ax1)
    ax1.set_title("Distribution of Review Lengths")
    
    # Review Length by Rating
    sns.boxplot(data=df, x='rating', y='review_length', ax=ax2)
    ax2.set_title("Review Length by Rating")
    
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def plot_feature_importance(df, save_path="plots/feature_importance.png"):
    """Visualize feature correlations with rating."""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    correlations = df[numeric_cols].corr()['rating'].sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    correlations.plot(kind='bar')
    plt.title("Feature Correlations with Rating")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def detect_outliers(df, columns):
    """Detect outliers using IQR method."""
    outliers_dict = {}
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
        outliers_dict[col] = {
            'count': len(outliers),
            'percentage': (len(outliers) / len(df)) * 100,
            'bounds': (lower_bound, upper_bound)
        }
    return outliers_dict

def generate_full_analysis(df):
    """Generate all analyses and visualizations."""
    # Create plots directory if it doesn't exist
    import os
    os.makedirs("plots", exist_ok=True)
    
    # Generate all analyses
    summary_stats = generate_summary_statistics(df)
    plot_rating_distribution(df)
    plot_sentiment_analysis(df)
    plot_review_length_analysis(df)
    plot_feature_importance(df)
    
    # Detect outliers in numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    outliers_info = detect_outliers(df, numeric_cols)
    
    return {
        'summary_statistics': summary_stats,
        'outliers_info': outliers_info
    }

if __name__ == "__main__":
    # Load the cleaned data
    df = pd.read_csv("cleaned_customer_reviews.csv")
    
    # Generate full analysis
    analysis_results = generate_full_analysis(df)
    
    # Print summary of findings
    print("Analysis complete. Visualizations saved in 'plots' directory.")
    print("\nOutlier Summary:")
    for col, info in analysis_results['outliers_info'].items():
        print(f"{col}: {info['count']} outliers ({info['percentage']:.2f}%)")
```

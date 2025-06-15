# Marketing Analytics Project

A comprehensive project for analyzing customer reviews and engagement data to extract actionable business insights using data preprocessing, visualization, sentiment analysis, and SQL-based data integration.

---

## 🎯 Project Objectives

The primary goals of this project are:
- To perform a comprehensive analysis of customer behavior, from initial engagement to post-purchase reviews.
- To identify key drivers of customer satisfaction and dissatisfaction through sentiment analysis of reviews.
- To build a unified data model by integrating various data sources (e.g., customer data, product information, engagement metrics).
- To create visualizations and a dashboard to present key findings to stakeholders.
- To provide actionable recommendations for improving marketing strategies and product offerings.

---

## 💾 Data Sources

This project utilizes data from multiple sources to create a holistic view of the customer journey. The primary data sources include:
- **Customer Data**: Information about customer demographics and purchase history (`dim_customers.sql`).
- **Product Data**: Details about the products offered (`dim_products.sql`).
- **Engagement Data**: Metrics on user interactions with the marketing channels, such as clicks, views, and session duration (`fact_engagement_data.sql`).
- **Customer Reviews**: Textual feedback and ratings provided by customers (`fact_customer_reviews.sql`).
- **Customer Journey Data**: A chronological record of customer touchpoints (`fact_customer_journey.sql`).

These datasets are processed and integrated to create the final analytical dataset.

---

## 🛠️ Methodologies & Analysis Techniques

The analysis was conducted using a combination of data processing techniques, statistical analysis, and machine learning.

1.  **Data Cleaning & Preprocessing (`data_cleaning.py`)**:
    -   Handled missing values, duplicates, and inconsistencies in the raw data.
    -   Performed feature engineering to create new variables for analysis.
    -   Detected and treated outliers using the Interquartile Range (IQR) method.

2.  **Sentiment Analysis (`customer_reviews_enrichment.py`)**:
    -   Utilized the TextBlob library to perform sentiment analysis on customer reviews.
    -   Classified reviews into positive, negative, and neutral categories based on polarity scores.
    -   Extracted subjective opinions from the review text to identify specific points of feedback.

3.  **Exploratory Data Analysis (EDA) (`eda.ipynb`)**:
    -   Conducted summary statistics to understand data distributions.
    -   Created visualizations to uncover patterns, such as:
        -   Distribution of customer ratings.
        -   Correlation between sentiment polarity and ratings.
        -   Analysis of review length and content.

4.  **SQL-Based Data Integration**:
    -   Developed SQL scripts to extract, transform, and load data from a relational database.
    -   Created dimension and fact tables to build a star schema for efficient querying and analysis.

---

## 📈 Key Findings

*(Please provide a summary of the key insights and results from your analysis. For example:)*
- **Finding 1:** A strong positive correlation was found between positive sentiment in reviews and higher customer ratings.
- **Finding 2:** The most common theme in negative reviews was related to "shipping delays" and "product quality".
- **Finding 3:** Customers who engaged with more than three marketing touchpoints had a 25% higher conversion rate.
- **Finding 4:** The average sentiment polarity for Product X was significantly lower than for other products, indicating potential issues.

---

## 📊 Visualizations

- Customer rating distribution
- Sentiment polarity vs. ratings
- Review length by rating
- Additional insights are available in the `PowerBI Dashboard.pbix` file and the `Review 1 Presentation.pptx`.

---

## 📂 Project Structure

```
Marketing-Analytics/
├── data_cleaning.py                         # Data preprocessing and cleaning scripts
├── analysis_utils.py                        # Utilities for analysis and visualization
├── eda.ipynb                                # Exploratory Data Analysis (EDA) notebook
├── customer_reviews_enrichment.py           # Sentiment analysis and review enrichment
├── Review 1 Presentation.pptx               # Project presentation slides
├── PowerBI Dashboard.pbix                   # Interactive PowerBI dashboard
├── requirements.txt                         # Python dependencies
├── README.md                                # Project documentation
├── fact_customer_reviews_with_sentiment.csv # Processed review data with sentiment
└── SQL Queries/                             # Database query scripts
    ├── dim_customers.sql
    ├── dim_products.sql
    ├── fact_customer_journey.sql
    ├── fact_customer_reviews.sql
    └── fact_engagement_data.sql
```

---

## 🚀 Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Mohammadosama55/Marketing-Analytics.git
    cd Marketing-Analytics
    ```

2.  **Set up a database:**
    -   This project assumes a SQL database. You will need to set up a database and import your raw data.
    -   Update the connection strings in the Python scripts (`analysis_utils.py`, `customer_reviews_enrichment.py`) to point to your database.

3.  **Run the SQL queries:**
    -   Execute the scripts in the `SQL Queries/` directory to create the necessary tables (dimensions and facts).

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the data processing pipeline:**
    ```bash
    python data_cleaning.py
    python customer_reviews_enrichment.py
    ```

6.  **Explore the analysis:**
    -   Open the EDA notebook to see the exploratory analysis:
      ```bash
      jupyter notebook eda.ipynb
      ```
    -   Open `PowerBI Dashboard.pbix` in Power BI Desktop to view the interactive dashboard.

---

## 🔧 Requirements

- Python 3.8+
- pandas >= 1.5.0
- numpy >= 1.21.0
- textblob >= 0.15.3
- seaborn >= 0.12.0
- matplotlib >= 3.5.0

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## ❓ Questions & Contributions


2. Exploratory Data Analysis (`eda.ipynb`):
   - Generates summary statistics
   - Creates visualizations for:
     - Rating distribution
     - Sentiment analysis
     - Review length analysis

3. Review Enrichment (`customer_reviews_enrichment.py`):
   - Performs sentiment analysis
   - Extracts additional features from review text

## Key Features
- Comprehensive data cleaning and preprocessing
- Feature engineering and selection
- Statistical analysis and insights
- Visual representations of key findings
- SQL integration for data extraction

## Visualizations
The project includes several visualizations:
- Distribution of customer ratings
- Sentiment polarity vs ratings
- Review length analysis by rating
- Additional insights in the presentation file


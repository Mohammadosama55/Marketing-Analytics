# Marketing Analytics Project

This project focuses on analyzing customer reviews and engagement data to derive meaningful insights through data preprocessing, visualization, and statistical analysis.

## Project Structure
```
Marketing-Analytics/
├── data_cleaning.py                        # Data preprocessing and cleaning
├── analysis_utils.py                       # Analysis and visualization utilities
├── eda.ipynb                              # Exploratory Data Analysis notebook
├── customer_reviews_enrichment.py          # Review sentiment analysis
├── Review 1 Presentation.pptx             # Project presentation
├── requirements.txt                        # Project dependencies
├── README.md                              # Project documentation
├── fact_customer_reviews_with_sentiment.csv # Processed review data
└── SQL Queries:                           # Database queries
    ├── dim_customers.sql
    ├── dim_products.sql
    ├── fact_customer_journey.sql
    ├── fact_customer_reviews.sql
    └── fact_engagement_data.sql
```

## Requirements
```python
pandas>=1.5.0
numpy>=1.21.0
textblob>=0.15.3
seaborn>=0.12.0
matplotlib>=3.5.0
```

## Setup Instructions
1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run data cleaning:
   ```bash
   python data_cleaning.py
   ```
4. Open and run the Jupyter notebook:
   ```bash
   jupyter notebook eda.ipynb
   ```

## Data Processing Pipeline
1. Data Cleaning (`data_cleaning.py`):
   - Handles missing values
   - Removes duplicates
   - Performs feature engineering
   - Handles outliers using IQR method

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

## Authors
[Your Name/Team]

## License
[Specify License]
import pandas as pd
from analysis_utils import generate_full_analysis

df = pd.read_csv("fact_customer_reviews_with_sentiment.csv")
analysis_results = generate_full_analysis(df)
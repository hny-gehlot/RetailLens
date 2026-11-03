# RetailLens — Retail Sales Intelligence

RetailLens is a retail analytics project built using the **UCI Online Retail dataset**. The goal is to investigate retail transaction data, identify business patterns, and generate insights that can support better business decisions.

## Business Problem

Retail businesses generate large amounts of transaction data. However, raw data often contains missing values, duplicate records, cancellations, and unusual transactions.

RetailLens aims to analyse this data to understand:

- Overall sales and revenue performance
- Product demand and purchasing patterns
- Customer purchasing behaviour
- Sales trends over time
- Cancellations and unusual transactions

## Dataset

**Source:** [UCI Machine Learning Repository — Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail)

The dataset contains 541,909 transaction records from a UK-based online retailer.

It includes:

- Invoice number
- Product code
- Product description
- Quantity
- Invoice date
- Unit price
- Customer ID
- Country

## Technologies

- Python
- Pandas
- Git and GitHub
- SQL (planned)
- Data visualization tools (planned)

## Project Structure

```text
RetailLens/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── reports/
│   └── data_quality_report.md
├── src/
│   ├── main.py
│   ├── inspect_data.py
│   └── clean_data.py
├── .gitignore
└── README.md
```

## Current Progress

### Phase 1 — Data Inspection and Quality Assessment

- Inspected dataset structure and data types.
- Identified missing values.
- Investigated exact duplicate records.
- Examined cancellation transactions.
- Investigated zero-price and negative-price records.
- Calculated transaction-level revenue.
- Documented data quality findings.

### Phase 2 — Data Cleaning

- Implemented a Python data cleaning pipeline using Pandas.
- Removed 5,268 exact duplicate records.
- Retained records with missing CustomerIDs and descriptions.
- Preserved cancellation and unusual transactions for further analysis.
- Calculated transaction-level revenue.
- Classified transactions based on positive, negative, and zero revenue.
- Exported the cleaned dataset as a CSV file.

**Current processed dataset:** 536,641 records.

## Data Handling Decisions

- Exact duplicate records are removed from the analytical dataset.
- Missing CustomerIDs and descriptions are retained rather than automatically deleted.
- Cancellation transactions are preserved for separate analysis.
- Negative-price accounting adjustments are retained and identified for investigation.
- Zero-price transactions are retained for further investigation.
- The original raw dataset remains unchanged.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/hny-gehlot/RetailLens.git
cd RetailLens
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install pandas openpyxl
```

### 4. Add the dataset

Download the Online Retail dataset from the UCI repository and place the Excel file inside:

```text
data/raw/Online Retail.xlsx
```

### 5. Run the inspection script

```bash
python src/inspect_data.py
```

### 6. Run the cleaning pipeline

```bash
python src/clean_data.py
```

The processed CSV file will be generated at:

```text
data/processed/online_retail_cleaned.csv
```

## Future Improvements

- Exploratory Data Analysis (EDA)
- Product and customer purchasing analysis
- SQL-based retail data analysis
- Sales trend visualization
- Interactive business intelligence dashboard
- Customer segmentation and predictive modelling

## Project Goal

Build a reproducible retail analytics project that demonstrates practical skills in data cleaning, exploratory data analysis, SQL, business intelligence, and predictive modelling.
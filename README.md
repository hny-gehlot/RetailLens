# RetailLens — Retail Sales Intelligence

RetailLens is a data analytics project built using the UCI Online Retail dataset. The goal is to investigate retail transaction data, identify business patterns, and generate insights that can support better business decisions.

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

The dataset contains approximately 541,909 transaction records from a UK-based online retailer.

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
│   ├── data_quality_report.md
│   └── .gitkeep
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

In progress.

## Data Handling Decisions

- Exact duplicate records are removed from the analytical dataset.
- Missing CustomerIDs and descriptions are retained.
- Cancellation transactions are preserved for separate analysis.
- Negative-price accounting adjustments are flagged separately.
- Zero-price transactions are retained for further investigation.
- The original raw dataset remains unchanged.

## How to Run

The cleaning pipeline is currently under development. Instructions for running the completed pipeline will be added here.

## Project Goal

Build a reproducible retail analytics project that demonstrates practical skills in data cleaning, exploratory data analysis, SQL, business intelligence, and eventually predictive modelling.


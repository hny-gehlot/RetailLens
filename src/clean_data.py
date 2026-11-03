
import pandas as pd
from pathlib import Path


# ==========================================
# 1. LOAD THE ORIGINAL DATASET
# ==========================================

df = pd.read_excel("data/raw/Online Retail.xlsx")

print("\n========== DATASET OVERVIEW ==========")

print("\nOriginal dataset shape:")
print(df.shape)


# ==========================================
# 2. DUPLICATE REMOVAL
# ==========================================

print("\n========== DUPLICATE ANALYSIS ==========")

duplicate_count = df.duplicated().sum()

print("\nExact duplicate rows found:")
print(duplicate_count)

# Remove exact duplicate rows
df = df.drop_duplicates().copy()

print("\nDataset shape after duplicate removal:")
print(df.shape)

print("\nRemaining duplicate rows:")
print(df.duplicated().sum())


# ==========================================
# 3. REVENUE CALCULATION
# ==========================================

print("\n========== REVENUE ANALYSIS ==========")

# Calculate revenue for each transaction
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

total_revenue = df["Revenue"].sum()

print("\nTotal dataset revenue:")
print(round(total_revenue, 2))


# ==========================================
# 4. MISSING VALUE ANALYSIS
# ==========================================

print("\n========== MISSING VALUE ANALYSIS ==========")

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nTotal missing cells:")
print(df.isnull().sum().sum())

# Investigate records with missing CustomerIDs
missing_customers = df[df["CustomerID"].isnull()].copy()

missing_customers_revenue = missing_customers["Revenue"].sum()

missing_customer_percentage = (
    missing_customers_revenue / total_revenue
) * 100

print("\nRecords with missing CustomerIDs:")
print(len(missing_customers))

print("\nRevenue from records with missing CustomerIDs:")
print(round(missing_customers_revenue, 2))

print("\nPercentage of revenue from missing CustomerIDs:")
print(round(missing_customer_percentage, 2), "%")


# Investigate records with missing descriptions
missing_descriptions = df[df["Description"].isnull()].copy()

print("\nRecords with missing descriptions:")
print(len(missing_descriptions))

print("\nUnique StockCodes with missing descriptions:")
print(missing_descriptions["StockCode"].nunique())

print("\nRevenue from records with missing descriptions:")
print(round(missing_descriptions["Revenue"].sum(), 2))

print("\nMost common StockCodes with missing descriptions:")
print(missing_descriptions["StockCode"].value_counts().head(10))


# ==========================================
# 5. PRICE ANALYSIS
# ==========================================

print("\n========== PRICE ANALYSIS ==========")

# Investigate zero-price records
zero_price = df[df["UnitPrice"] == 0].copy()

print("\nRecords with zero UnitPrice:")
print(len(zero_price))

print("\nMost common descriptions in zero-price records:")
print(zero_price["Description"].value_counts().head(10))

print("\nMissing CustomerIDs in zero-price records:")
print(zero_price["CustomerID"].isnull().sum())

print("\nRevenue from zero-price records:")
print(round(zero_price["Revenue"].sum(), 2))


# Investigate negative-price records
negative_price = df[df["UnitPrice"] < 0].copy()

print("\nRecords with negative UnitPrice:")
print(len(negative_price))

print("\nNegative-price records:")
print(
    negative_price[
        [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "UnitPrice",
            "CustomerID",
            "Country"
        ]
    ].to_string(index=False)
)

print("\nRevenue from negative-price records:")
print(round(negative_price["Revenue"].sum(), 2))


# ==========================================
# 6. QUANTITY AND CANCELLATION ANALYSIS
# ==========================================

print("\n========== TRANSACTION ANALYSIS ==========")

# Identify all negative-quantity records
negative_quantity = df[df["Quantity"] < 0].copy()

print("\nTotal negative-quantity records:")
print(len(negative_quantity))

# Identify cancellation invoices
cancellation_mask = (
    df["InvoiceNo"].astype(str).str.startswith("C")
)

cancellations = df[
    (df["Quantity"] < 0) & cancellation_mask
].copy()

print("\nNegative quantities with C invoices:")
print(len(cancellations))

# Identify negative quantities without C prefix
other_negative_quantity = df[
    (df["Quantity"] < 0) & (~cancellation_mask)
].copy()

print("\nNegative quantities without C invoices:")
print(len(other_negative_quantity))

print("\nSample unusual negative-quantity records:")
print(
    other_negative_quantity[
        [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "UnitPrice",
            "CustomerID"
        ]
    ].head(10)
)

print("\nRevenue from all negative-quantity records:")
print(round(negative_quantity["Revenue"].sum(), 2))


# ==========================================
# 7. REVENUE CLASSIFICATION
# ==========================================

print("\n========== REVENUE CLASSIFICATION ==========")

# Separate records based on calculated revenue
positive_revenue = df[df["Revenue"] > 0]

negative_revenue = df[df["Revenue"] < 0]

zero_revenue = df[df["Revenue"] == 0]

print("\nPositive revenue records:")
print(len(positive_revenue))

print("\nNegative revenue records:")
print(len(negative_revenue))

print("\nZero revenue records:")
print(len(zero_revenue))

print("\nTotal positive revenue:")
print(round(positive_revenue["Revenue"].sum(), 2))

print("\nTotal negative revenue:")
print(round(negative_revenue["Revenue"].sum(), 2))

print("\nNet dataset revenue:")
print(round(df["Revenue"].sum(), 2))


# ==========================================
# 8. NEGATIVE REVENUE INVESTIGATION
# ==========================================

print("\n========== NEGATIVE REVENUE INVESTIGATION ==========")

negative_revenue_cancellations = negative_revenue[
    negative_revenue["InvoiceNo"].astype(str).str.startswith("C")
]

other_negative_revenue = negative_revenue[
    ~negative_revenue["InvoiceNo"].astype(str).str.startswith("C")
]

print("\nNegative revenue with C invoices:")
print(len(negative_revenue_cancellations))

print("\nNegative revenue without C invoices:")
print(len(other_negative_revenue))

print("\nRevenue from C invoices:")
print(round(negative_revenue_cancellations["Revenue"].sum(), 2))

print("\nRevenue from non-C negative records:")
print(round(other_negative_revenue["Revenue"].sum(), 2))


# ==========================================
# 9. SAVE THE PROCESSED DATASET
# ==========================================

print("\n========== SAVING PROCESSED DATA ==========")

output_directory = Path("data/processed")

output_directory.mkdir(parents=True, exist_ok=True)

output_path = output_directory / "online_retail_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nProcessed dataset saved successfully:")
print(output_path)

print("\nFinal dataset shape:")
print(df.shape)

print("\nCleaning process completed.")

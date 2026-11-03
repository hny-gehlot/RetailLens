import pandas as pd

# Load the original dataset
df = pd.read_excel("data/raw/Online Retail.xlsx")


# ==========================================
# 1. DATASET OVERVIEW
# ==========================================

print("\n========== DATASET OVERVIEW ==========")

print("\nFirst five records:")
print(df.head())

print("\nDataset dimensions:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset information:")
df.info()

print("\nNumerical summary:")
print(df.describe())

# ==========================================
# 2. MISSING VALUE ANALYSIS
# ==========================================

print("\n========== MISSING VALUE ANALYSIS ==========")

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nTotal missing cells:")
print(df.isnull().sum().sum())

print("\nPercentage of missing values in each column:")
print((df.isnull().mean() * 100).round(2))

# ==========================================
# 3. DUPLICATE ANALYSIS
# ==========================================

print("\n========== DUPLICATE ANALYSIS ==========")

# Count exact duplicate rows
duplicate_count = df.duplicated().sum()

print("\nTotal exact duplicate rows:")
print(duplicate_count)

# Store duplicate records for further investigation
duplicates = df[df.duplicated()].copy()

print("\nFirst five duplicate records:")
print(duplicates.head())

# Check how many duplicate records have missing CustomerIDs
print("\nMissing CustomerIDs in duplicate records:")
print(duplicates["CustomerID"].isnull().sum())

# Count unique invoices containing duplicate records
print("\nUnique invoices containing duplicate records:")
print(duplicates["InvoiceNo"].nunique())

# ==========================================
# 4. TRANSACTION ANALYSIS
# ==========================================

print("\n========== TRANSACTION ANALYSIS ==========")

# Identify records with negative quantities
negative_qty = df[df["Quantity"] < 0]

print("\nRecords with negative quantities:")
print(len(negative_qty))

# Identify cancelled invoices (InvoiceNo starts with C)
cancelled_invoices = df[
    df["InvoiceNo"].astype(str).str.startswith("C")
]

print("\nRecords belonging to cancelled invoices:")
print(len(cancelled_invoices))

# Check negative quantities within cancelled invoices
print("\nNegative quantities in cancelled invoices:")
print((cancelled_invoices["Quantity"] < 0).sum())

# Identify negative quantities without a C prefix
other_negative = df[
    (df["Quantity"] < 0) &
    (~df["InvoiceNo"].astype(str).str.startswith("C"))
]

print("\nNegative quantities without a C prefix:")
print(len(other_negative))

print("\nSample unusual negative quantity records:")
print(
    other_negative[
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

# ==========================================
# 5. PRICE ANALYSIS
# ==========================================

print("\n========== PRICE ANALYSIS ==========")

# Identify records with zero unit price
zero_price = df[df["UnitPrice"] == 0]

print("\nRecords with zero unit price:")
print(len(zero_price))

print("\nDescriptions of zero-price records:")
print(zero_price["Description"].value_counts().head(10))

print("\nMissing CustomerIDs in zero-price records:")
print(zero_price["CustomerID"].isnull().sum())

# Identify records with negative unit price
negative_price = df[df["UnitPrice"] < 0]

print("\nRecords with negative unit price:")
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
    ]
)

# ==========================================
# 6. DUPLICATE REVENUE INVESTIGATION
# ==========================================

print("\n========== DUPLICATE REVENUE INVESTIGATION ==========")

# Create a copy of duplicate records
duplicates = df[df.duplicated()].copy()

# Calculate revenue for duplicate records
duplicates["Revenue"] = (
    duplicates["Quantity"] * duplicates["UnitPrice"]
)

print("\nRevenue represented by duplicate rows:")
print(round(duplicates["Revenue"].sum(), 2))

print("\nTotal quantity in duplicate rows:")
print(duplicates["Quantity"].sum())

print("\nNegative quantity records among duplicates:")
print((duplicates["Quantity"] < 0).sum())

print("\nInvoices with the most duplicate rows:")
print(duplicates["InvoiceNo"].value_counts().head(10))
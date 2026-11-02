import pandas as pd

# Load the original dataset
df = pd.read_excel("data/raw/Online Retail.xlsx")

# Display the original dataset dimensions
print("Original dataset shape:")
print(df.shape)

# Count duplicate rows before cleaning
duplicate_count = df.duplicated().sum()

print("\nDuplicate rows found:")
print(duplicate_count)

# Remove exact duplicate rows
df = df.drop_duplicates()

# Display dataset after removing duplicates
print("\nDataset after removing duplicates:")
print(df.shape)

# Verify that duplicates have been removed
print("\nRemaining duplicate rows:")
print(df.duplicated().sum())

# Check Missing values after removing duplicates
print("\nMissing values after removing duplicates:")
print(df.isnull().sum())

# Calculate total missing cells
print("\nTotal missing cells:")
print(df.isnull().sum().sum())

# Separate records with missing customer IDs
missing_customers = df[df["CustomerID"].isnull()]

print("\nRecords of missing customer IDs:")
print(missing_customers.head(10))

print("\nTotal number of missing customers IDs:")
print(len(missing_customers))

# Calculate revenue for each record
missing_customers = df[df["CustomerID"].isnull()].copy()

missing_customers["Revenue"] = (missing_customers["Quantity"] * missing_customers["UnitPrice"])

# Calculate total revenue
print("\nTotal revenue from records with missing CustomerIDs:")
print(missing_customers["Revenue"].sum())

# Calculate revenue of the entire clean dataset
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

total_revenue = df["Revenue"].sum()

missing_customer_revenue = missing_customers["Revenue"].sum()

# Calculate percentage calculation
missing_customer_percentage = (missing_customer_revenue/total_revenue) * 100

print("\nTotal dataset revenue:")
print(round(total_revenue, 2))

print("\nRevenue from missing CustomerIDs:")
print(round(missing_customer_revenue, 2))

print("\nPercentage of revenue from missing CustomerIDs:")
print(round(missing_customer_percentage, 2), "%")

# Separate records with missing descriptions
missing_descriptions = df[df["Description"].isnull()].copy()

print("\nRecords with missing descriptions:")
print(len(missing_descriptions))

print("\nUnique StockCodes with missing descriptions:")
print(missing_descriptions["StockCode"].nunique())

print("\nRevenue from records with missing descriptions:")
print((missing_descriptions["Quantity"] * missing_descriptions["UnitPrice"]).sum())

print("\nMost common StockCodes:")
print(missing_descriptions["StockCode"].value_counts().head(10))

# Calculate revenue for zero price records
zero_price = df[df["UnitPrice"]==0].copy()

zero_price_revenue = (zero_price["Quantity"] * zero_price["UnitPrice"])

print("\nZero price record revenue:")
print(zero_price_revenue.sum())

# Inspect negative price records
negative_price = df[df["UnitPrice"]<0]

print("\nNegative price records:")
print(negative_price.to_string(index=False))

# Identify negative quantity records
negative_quantity = df[df["Quantity"] < 0].copy()

print("\nTotal negative quantity records:")
print(len(negative_quantity))

print("\nNegative quantity records with C invoices:")
print(negative_quantity["InvoiceNo"].astype(str).str.startswith("C").sum())

print("\nNegative quantity records without C invoices:")
print((~negative_quantity["InvoiceNo"].astype(str).str.startswith("C")).sum())

print("\nRevenue from negative quantity records:")
print(negative_quantity["Revenue"].sum())

# Separate positive and negative revenue records

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

# Investigate negative revenue records

negative_revenue = df[df["Revenue"] < 0].copy()

cancellations = negative_revenue[negative_revenue["InvoiceNo"].astype(str).str.startswith("C")]

other_negative_revenue = negative_revenue[~negative_revenue["InvoiceNo"].astype(str).str.startswith("C")]

print("\nNegative revenue with C invoices:")
print(len(cancellations))

print("\nNegative revenue without C invoices:")
print(len(other_negative_revenue))

print("\nRevenue from C invoices:")
print(round(cancellations["Revenue"].sum(), 2))

print("\nRevenue from non-C negative records:")
print(round(other_negative_revenue["Revenue"].sum(), 2))
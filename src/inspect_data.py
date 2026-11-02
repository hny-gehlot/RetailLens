import pandas as pd

df = pd.read_excel("data/raw/Online Retail.xlsx")

print("First five rows:")
print(df.head())

print("\nColumn names:")
print(df.columns)

print("\nSize of the data:")
print(df.shape)

print("\nInformation of the data:")
print(df.info())

print("\nDescribe the data numerically:")
print(df.describe())

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nTotal missing values:")
print(df.isnull().sum().sum())

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

duplicates =df[df.duplicated()]

print("\nDuplicate records:")
print(duplicates.head(10))

print("\nTotal duplicate records:")
print(len(duplicates))

print("\nMissing cutomerIDs in duplicates:")
print(duplicates["CustomerID"].isnull().sum())

print("\nUnique invoices:")
print(df["InvoiceNo"].nunique())

print("\nMost common invoice numbers:")
print(df["InvoiceNo"].value_counts().head(10))

invoice = df[df["InvoiceNo"]==573585]
print("\nInvoice 573585:")
print(invoice)

print("\nNumber of rows in this invoice:")
print(len(invoice))

print("\nNumber of unique product it contains:")
print(invoice["StockCode"].nunique())

print(type(df["InvoiceNo"].iloc[0]))
print(repr(df["InvoiceNo"].iloc[0]))
print(df["InvoiceNo"].head())

print(df["InvoiceNo"].astype(str).str.strip().eq("573585").sum())

negative_qty = df[df["Quantity"]<0]

print("\nNegative quantity is:")
print(negative_qty.head())

print("\nNumber of negative quantity:")
print(len(negative_qty))

cancelled_invoices = df[df["InvoiceNo"].astype(str).str.startswith("C")]

print("\nInvoices starts with C:")
print(cancelled_invoices.head())

print("\nNumber of cancelled invoices:")
print(len(cancelled_invoices))

print("\nThe negative quantities in these invoices:")
print((cancelled_invoices["Quantity"]<0).sum())

other_negative = df[
    (df["Quantity"]<0) & (~df["InvoiceNo"].astype(str).str.startswith("C"))
]

print("\nNegative quanitites without C prefix:")
print(other_negative.head(10))

print("\nNumber of other negatives:")
print(len(other_negative))

print("\nSummary of unusual negative quantity records:")
print(other_negative[[
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "CustomerID"
]].head(20))

print("\nMissing unit price values:")
print(other_negative["UnitPrice"].isnull().sum())

print("\nZero unit price values:")
print((other_negative["UnitPrice"]==0).sum())

print("\nUnique stock codes in unusual records:")
print(other_negative["StockCode"].nunique())

print("\nMost common stock codes:")
print(other_negative["StockCode"].value_counts().head(10))

zero_price = df[df["UnitPrice"]==0]

print("\nRecords with zero unit price:")
print(len(zero_price))

negative_price = df[df["UnitPrice"]<0]

print("\nRecords with negatve unit price:")
print(negative_price.head(10))

print("\nTotal negative price:")
print(len(negative_price))

print(zero_price.head(10))

print("\nMost common descriptions:")
print(zero_price["Description"].value_counts().head(10))

print("\nMissing customerIDs:")
print(zero_price["CustomerID"].isnull().sum())

print("\nQuantity Summary:")
print(zero_price["Quantity"].describe())

print("\nNegative quantities:")
print((zero_price["Quantity"]<0).sum())

print("\nPositive Quantites:")
print((zero_price["Quantity"]>0).sum())

print("\nZero Quanitites:")
print((zero_price["Quantity"]==0).sum())

print("\nInvoice numbers beginning with C")
print(zero_price["InvoiceNo"].astype(str).str.startswith("C").sum())

print("\nMissing descriptions:")
print(zero_price["Description"].isnull().sum())

duplicates = df[df.duplicated()].copy()

duplicates["Revenue"] = (
    duplicates["Quantity"] * duplicates["UnitPrice"]
)

print("\nRevenue in dupilcate records:")
print(duplicates["Revenue"].sum())

print("\nTotal quantity in duplicate recoreds:")
print(duplicates["Quantity"].sum())

print("\nNegative quantity in duplicate records:")
print((duplicates["Quantity"]<0).sum())

print(duplicates["InvoiceNo"].value_counts().head(10))

print("\nUnique invoices with duplicates:")
print(duplicates["InvoiceNo"].nunique())

i = 555524
invoice_sample = df[df["InvoiceNo"]==i]
print(invoice_sample)

print(invoice_sample["StockCode"].value_counts().head(10))

print("\nTotal rows in this invoice sample:")

print(len(invoice_sample))

print("/nExact duplicate rows in this invoice:")
print(invoice_sample.duplicated().sum())

print(invoice_sample["StockCode"].dtype)
print(type(invoice_sample["StockCode"].iloc[0]))
print(repr(invoice_sample["StockCode"].iloc[0]))
print(invoice_sample[invoice_sample["StockCode"] == 22698])

print(invoice_sample["StockCode"].unique())

print("Exact duplicates:")
print(invoice_sample.duplicated().sum())

unique_invoice_rows = invoice_sample.drop_duplicates()

print("\nRows after removing exact duplicates:")
print(len(unique_invoice_rows))

print("\nProduct counts after removing exact duplicates:")
print(unique_invoice_rows["StockCode"].value_counts().head(10))

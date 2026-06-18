import pandas as pd
import sqlite3

# Extract
df = pd.read_csv("sales.csv")

print("Original Data")
print(df.head())

# Transform
df["Total_Sales"] = df["Quantity"] * df["Price"]

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("\nTransformed Data")
print(df.head())

print("\nChecking Null Values")

print(df.isnull().sum())

print("\nChecking Duplicates")

print(df.duplicated().sum())

# Load
conn = sqlite3.connect("sales.db")

df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\nData Loaded Successfully into SQLite")

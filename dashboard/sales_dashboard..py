import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# Connect Database
conn = sqlite3.connect("sales.db")

# Read Data
df = pd.read_sql(
    "SELECT * FROM sales",
    conn
)

conn.close()


# KPI Calculations

total_revenue = df["Total_Sales"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order_ID"].count()


print("Total Revenue:", total_revenue)
print("Total Quantity:", total_quantity)
print("Total Orders:", total_orders)


# Create Dashboard

plt.figure(figsize=(12,8))


# 1. Revenue by Category

plt.subplot(2,2,1)

category_sales = (
    df.groupby("Category")["Total_Sales"]
    .sum()
)

category_sales.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")


# 2. Top Products

plt.subplot(2,2,2)

top_products = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

top_products.plot(kind="bar")

plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity")


# 3. Sales Trend

plt.subplot(2,2,3)

daily_sales = (
    df.groupby("Order_Date")["Total_Sales"]
    .sum()
)

daily_sales.plot(kind="line")

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")


# 4. KPI Summary

plt.subplot(2,2,4)

plt.axis("off")

summary = f"""
RETAIL SALES DASHBOARD

Total Revenue:
${total_revenue}

Total Orders:
{total_orders}

Items Sold:
{total_quantity}
"""

plt.text(
    0.1,
    0.5,
    summary,
    fontsize=12
)


plt.tight_layout()

plt.savefig(
    "sales_dashboard.png"
)

plt.show()

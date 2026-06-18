import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")

# Total Revenue
query1 = """
SELECT SUM(Total_Sales) AS Total_Revenue
FROM sales
"""

# Revenue by Category
query2 = """
SELECT Category,
       SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Category
"""

# Top Selling Products
query3 = """
SELECT Product,
       SUM(Quantity) AS Quantity_Sold
FROM sales
GROUP BY Product
ORDER BY Quantity_Sold DESC
"""

print("\nTOTAL REVENUE")
print(pd.read_sql(query1, conn))

print("\nREVENUE BY CATEGORY")
print(pd.read_sql(query2, conn))

print("\nTOP SELLING PRODUCTS")
print(pd.read_sql(query3, conn))

conn.close()

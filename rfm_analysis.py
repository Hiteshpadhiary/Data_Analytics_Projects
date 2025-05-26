import pandas as pd
from datetime import datetime

df = pd.read_csv("Ecommerce_Orders_2025.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
snapshot_date = datetime(2025, 1, 1)

rfm = df.groupby("Customer ID").agg({
    "Order Date": lambda x: (snapshot_date - x.max()).days,
    "Order ID": "count",
    "Sales": "sum"
}).rename(columns={"Order Date": "Recency", "Order ID": "Frequency", "Sales": "Monetary"})

# Use .cat.codes for safe binning
rfm["R_Score"] = pd.qcut(rfm["Recency"], 4, duplicates='drop').cat.codes.map({0: 4, 1: 3, 2: 2, 3: 1})
rfm["F_Score"] = pd.qcut(rfm["Frequency"], 4, duplicates='drop').cat.codes + 1
rfm["M_Score"] = pd.qcut(rfm["Monetary"], 4, duplicates='drop').cat.codes + 1

rfm["RFM_Score"] = rfm["R_Score"].astype(str) + rfm["F_Score"].astype(str) + rfm["M_Score"].astype(str)

print(rfm.head())
rfm.to_csv("rfm_results.csv")




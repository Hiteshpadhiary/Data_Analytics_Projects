import pandas as pd

df = pd.read_csv("Ecommerce_Orders_2025.csv")  # replace with actual file if not already read
print("Available columns:", df.columns)
#churn_analysis
from datetime import datetime
df = pd.read_csv("Ecommerce_Orders_2025.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors='coerce')
last_date = datetime(2024, 9, 30)
churn_threshold = last_date - pd.Timedelta(days=90)  # Last 3 months
recent_purchases = df[df["Order Date"] > churn_threshold]
active_customers = recent_purchases["Customer ID"].unique()
all_customers = df["Customer ID"].unique()
at_risk_customers = set(all_customers) - set(active_customers)
churn_df = pd.DataFrame({"Customer ID": list(at_risk_customers), "Status": "At-Risk"})
churn_df.to_csv("churn_results.csv", index=False)
print(f"Total At-Risk Customers: {len(at_risk_customers)}")
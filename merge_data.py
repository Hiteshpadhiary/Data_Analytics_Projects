import pandas as pd
train = pd.read_csv("train.csv")
customer = pd.read_csv("customer.csv")
train["Customer ID"] = train["Customer ID"].str.strip()
customer["Customer ID"] = customer["Customer ID"].str.strip()
merged = pd.merge(train, customer, on="Customer ID", how="left")
print("Merged DataFrame Columns:", merged.columns.tolist())  # Debug line
merged.rename(columns={"Segment_y": "Segment"}, inplace=True)
sales_by_segment = merged.groupby("Segment")["Sales"].sum()
print(sales_by_segment)
sales_by_segment.to_csv("sales_by_segment.csv")
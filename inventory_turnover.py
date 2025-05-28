import pandas as pd
df = pd.read_csv("inventory_data.csv")
df["Turnover"] = df["Units Sold"] / df["Average Stock Level "]
print(df)
df.to_csv("inventory_turnover_results.csv")
import pandas as pd
df = pd.read_csv("train.csv")
sales_by_category = df.groupby("Category")["Sales"].sum()
print(sales_by_category)
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("train.csv")
sales_by_category = df.groupby ("Category")["Sales"].sum()
sales_by_category.plot(kind="bar",color="skyblue")
plt.title("sales by Category")
plt.xlabel("category")
plt.ylabel("Total Sales")
plt.savefig("sales_by_category.png")
plt.show()

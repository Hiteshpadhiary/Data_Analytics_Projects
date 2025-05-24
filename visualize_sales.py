import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("train.csv")
pivot = df.pivot_table(values="Sales", index="Category", columns="Region", aggfunc="sum")
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Sales by Category and Region")
plt.savefig("sales_heatmap.png")
plt.show()
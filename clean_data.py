import pandas as pd
df =pd.read_csv("train.csv")
print("missing Values:\n",df.isnull().sum())
df_cleaned = df.drop_duplicates()
print ("Duplicates REmoved:", len(df) - len (df_cleaned))
df_cleaned.to_csv("train_cleaned.csv",index=False)

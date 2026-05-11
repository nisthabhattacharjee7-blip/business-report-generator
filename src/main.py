import pandas as pd 


df = pd.read_csv("data/sales.csv")
print("\n == FULL DATA ==")
print(df)

print("\n == Data info ==")
print(df.info())

print("\n == Missing Values ==")
print(df.isnull().sum())

print("\n == DUBLICATES ==")
print(df.duplicated().sum())

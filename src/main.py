import pandas as pd 
from cleaner import clean_data

df = pd.read_csv("data/sales.csv")
df = clean_data(df)

print("\n=== ORIGINAL DATA ===")
print(df)

cleaned_df = clean_data(df)

print("\n=== CLEANED DATA ===")
print(cleaned_df)

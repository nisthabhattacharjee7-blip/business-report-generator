import pandas as pd 
from cleaner import clean_data
from analyzer import analyze_df 

df = pd.read_csv("data/sales.csv")
df = clean_data(df)

print("\n=== ORIGINAL DATA ===")
print(df)

cleaned_df = clean_data(df)

print("\n=== CLEANED DATA ===")
print(cleaned_df)

analysis = analyze_df(cleaned_df)
print("\n=== ANALYSIS REPORTS ===")

total_revenue, avg_revenue, top_products = analysis

print("\nTotal Revenue:", total_revenue)
print("Average Revenue:", avg_revenue)
print("Top Product:", top_products)


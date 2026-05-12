import pandas as pd 
from cleaner import clean_data
from analyzer import analyze_df 
from reporter import generate_report

df = pd.read_csv("data/sales.csv")

# original data 
print("\n=== ORIGINAL DATA ===")
print(df)

# clean data 
cleaned_df = clean_data(df)

print("\n=== CLEANED DATA ===")
print(cleaned_df)

analysis = analyze_df(cleaned_df)
print("\n=== ANALYSIS REPORTS ===")

generate_report(cleaned_df, analysis)

total_revenue, avg_revenue, top_products = analysis

print("\nTotal Revenue:", total_revenue)
print("Average Revenue:", avg_revenue)
print("Top Product:", top_products)


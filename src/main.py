import pandas as pd
import json

from cleaner import clean_data
from analyzer import analyze_df
from reporter import generate_report
from utils import log_message
from database import create_connection , create_table, insert_data 
from database import get_total_revenue
from visualizer import revenue_chart, category_chart

try:

    # Start pipeline
    log_message("Pipeline started")

    # Load CSV
    df = pd.read_csv("data/sales.csv")
    log_message("CSV loaded successfully")

    print("\n=== ORIGINAL DATA ===")
    print(df)

    # Clean data
    cleaned_df = clean_data(df)
    log_message("Data cleaned successfully")

    print("\n=== CLEANED DATA ===")
    print(cleaned_df)\
    
    # database setup 
    con = create_connection()
    create_table(con)
    print("\nDatabase setup completed successfully")
    
    # insert data into database
    insert_data(con, cleaned_df)
    print("\nData inserted into database successfully")
    
    # Get total revenue from database
    total_revenue = get_total_revenue(con)
    print(f"\nTotal Revenue from Database: {total_revenue}")

    # Analyze data
    analysis = analyze_df(cleaned_df)
    log_message("Data analyzed successfully")

    print("\n=== ANALYSIS REPORTS ===")

    # Generate reports
    generate_report(cleaned_df, analysis)
    log_message("Reports generated successfully")
    
    # Create revenue chart
    revenue_chart(cleaned_df)

    # Create category revenue chart
    category_chart(cleaned_df)
    
    # Load config file
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    print("\nCompany Name:", config["company_name"])

    # Unpack analysis results
    total_revenue, avg_revenue, top_products = analysis

    print("\nTotal Revenue:", total_revenue)
    print("Average Revenue:", avg_revenue)
    print("Top Product:", top_products)

    log_message("Pipeline completed successfully")


except Exception as e:

    print("Error:", e)

    log_message(f"Error occurred: {e}")
import json 

def generate_report(df,analysis):
    total_revenue, avg_revenue, top_products = analysis

    # Save report csv 
    df.to_csv("output/cleaned_data.csv", index=False)
    
    # create JSON report

    report = {
        "total_revenue": total_revenue,
        "average_revenue": avg_revenue,
        "top_product": top_products
    }

    with open("output/report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\nReport generated: output/report.json")
    
    # create text report
    with open("output/report.txt", "w") as txt_file:
        txt_file.write(f"Total Revenue: {total_revenue}\n")
        txt_file.write(f"Average Revenue: {avg_revenue}\n")
        txt_file.write(f"Top Product: {top_products}\n")

    print("\nReports generated successfully !")   

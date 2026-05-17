# Sales Analytics Pipeline

A modular Python-based data analytics pipeline that cleans raw sales data, stores it in a SQLite database, performs business analytics, generates visual insights, and automatically creates structured reports.

This project demonstrates foundational concepts used in real-world data engineering and analytics workflows including ETL pipelines, SQL integration, data visualization, logging systems, modular architecture, and automated reporting.

---

# Features

- Automated sales data cleaning
- Missing value and duplicate handling
- Revenue and business analytics
- SQLite database integration
- SQL-based analytical queries
- Data visualization using Matplotlib
- CSV, JSON, and text report generation
- Logging and error handling system
- Config-driven architecture
- Modular and maintainable code structure

---

# Tech Stack

- Python
- Pandas
- SQLite
- SQL
- Matplotlib
- JSON
- Python Logging Module
- Git & GitHub

---

# Project Architecture

```text
Raw CSV Data
      ↓
Data Cleaning Pipeline
      ↓
SQLite Database Storage
      ↓
SQL Analytics Queries
      ↓
Data Visualization
      ↓
Report Generation
      ↓
Logging & Configuration Management
```

---

# Project Structure

```text
sales-analytics-pipeline/
│
├── data/
│   └── sales.csv
│
├── output/
│   ├── cleaned_sales.csv
│   ├── report.json
│   ├── report.txt
│   ├── revenue_chart.png
│   ├── category_revenue_chart.png
│   └── category_pie_chart.png
│
├── logs/
│   └── .gitkeep
│
├── src/
│   ├── main.py
│   ├── cleaner.py
│   ├── analyzer.py
│   ├── reporter.py
│   ├── visualizer.py
│   ├── database.py
│   └── utils.py
│
├── sales.db
├── config.json
├── .gitignore
└── README.md
```

---

# Business Metrics Generated

The pipeline automatically calculates:

- Total Revenue
- Average Revenue per Order
- Top Selling Product
- SQL-based Revenue Analytics
- Category-wise Revenue Insights

---

# Data Cleaning Operations

The cleaning pipeline performs:

- Duplicate removal
- Missing value handling
- Invalid datatype correction
- Negative value filtering
- Numeric conversion for analysis

---

# Database Operations

The SQLite integration supports:

- Database creation
- Table creation
- Data insertion
- SQL analytics queries
- Persistent structured storage

---

# Data Visualizations

The project automatically generates:

- Revenue by Product Bar Chart
- Revenue by Category Bar Chart
- Revenue Distribution Pie Chart

Generated chart outputs are stored inside:

```text
output/
```

---

# Example SQL Query

```sql
SELECT SUM(quantity * price)
FROM sales;
```

---

# Generated Output Files

| File | Description |
|---|---|
| cleaned_sales.csv | Cleaned dataset |
| report.json | Structured business report |
| report.txt | Human-readable report |
| revenue_chart.png | Revenue by product visualization |
| category_revenue_chart.png | Revenue by category visualization |
| category_pie_chart.png | Revenue distribution pie chart |
| sales.db | SQLite database |
| app.log | Pipeline execution logs |

---

# How to Run

## Clone Repository

```bash
git clone <repository-url>
```

## Navigate to Project Directory

```bash
cd sales-analytics-pipeline
```

## Install Dependencies

```bash
pip install pandas matplotlib
```

## Run the Pipeline

```bash
python src/main.py
```

---

# Engineering Concepts Demonstrated

- ETL Pipeline Design
- Modular Programming
- SQL Integration
- Database Management
- Data Visualization
- Configuration Management
- Logging Systems
- Error Handling
- Data Transformation
- File-Based Data Processing

---

# Future Improvements

- Interactive dashboard using Streamlit
- Advanced SQL analytics
- API-based data ingestion
- Automated scheduling
- Cloud deployment
- Docker containerization
- Real-time data processing
- Multi-file ingestion system

---

# Author

Nistha Bhattacharjee

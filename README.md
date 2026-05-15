
# Business Report Generator

A modular Python-based data processing and reporting pipeline that cleans raw sales data, stores it in a SQLite database, performs business analytics, and automatically generates structured reports.

This project demonstrates foundational concepts used in real-world data engineering and analytics workflows including ETL pipelines, SQL integration, logging systems, modular architecture, and automated reporting.

---

# Features

- Automated sales data cleaning
- Missing value and duplicate handling
- Revenue and business analytics
- SQLite database integration
- SQL-based analytical queries
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
Report Generation
      ↓
Logging & Configuration Management
```

---

# Project Structure

```text
business_report_generator/
│
├── data/
│   └── sales.csv
│
├── output/
│   ├── cleaned_sales.csv
│   ├── report.json
│   └── report.txt
│
├── logs/
│   └── app.log
│
├── src/
│   ├── main.py
│   ├── cleaner.py
│   ├── analyzer.py
│   ├── reporter.py
│   ├── utils.py
│   └── database.py
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
cd business_report_generator
```

## Install Dependencies

```bash
pip install pandas
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
- Configuration Management
- Logging Systems
- Error Handling
- Data Transformation
- File-Based Data Processing

---

# Future Improvements

- Interactive data visualizations
- Dashboard integration
- API-based data ingestion
- Automated scheduling
- Cloud deployment
- Docker containerization
- Advanced SQL analytics
- Real-time data processing

---

# Author

Nistha Bhattacharjee

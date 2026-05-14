# Business Report Generator

A modular Python-based data processing and reporting pipeline designed to clean raw sales data, perform business analysis, and generate structured reports automatically.

This project demonstrates foundational data engineering and automation concepts including data cleaning, transformation, logging, configuration management, and report generation.

---

# Features

- Automated sales data cleaning
- Missing value and duplicate handling
- Revenue analysis and business metrics
- CSV, JSON, and text report generation
- Logging and error handling system
- Config-driven architecture
- Modular and maintainable code structure

---

# Tech Stack

- Python
- Pandas
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
Business Analysis
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
│   └── utils.py
│
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

---

# Data Cleaning Operations

The cleaning pipeline performs:

- Duplicate removal
- Missing value handling
- Invalid datatype correction
- Negative value filtering
- Numeric conversion for analysis

---

# How to Run

## Clone Repository

```bash
git clone <repository-url>
```

## Navigate to Project

```bash
cd business_report_generator
```

## Run the Pipeline

```bash
python src/main.py
```

---

# Output Files

The system automatically generates:

| File | Description |
|---|---|
| cleaned_sales.csv | Cleaned dataset |
| report.json | Structured business report |
| report.txt | Human-readable report |
| app.log | Pipeline execution logs |

---

# Engineering Concepts Demonstrated

- ETL Pipeline Design
- Modular Programming
- Configuration Management
- Logging Systems
- Error Handling
- Data Transformation
- File-Based Data Processing

---

# Future Improvements

- SQL database integration
- Interactive dashboards
- API-based data ingestion
- Automated scheduling
- Cloud deployment
- Docker containerization

---

# Author

Nistha Bhattacharjee

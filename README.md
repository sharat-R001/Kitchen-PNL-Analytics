# Kitchen PNL Analytics Dashboard

## Project Overview

This project focuses on analyzing Profit & Loss (PNL) data for a cloud kitchen business across multiple cities, stores, and revenue cohorts.

The objective was to perform:
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Business KPI analysis
- Interactive dashboard development

The final solution was developed using Python, Pandas, Plotly, and Streamlit.

---

# Business Problem

The dataset contains kitchen-level operational and financial metrics such as:
- Revenue
- Gross Margin
- EBITDA
- Order Count
- Discounts
- Food Cost
- Variance (food wastage)

The goal was to analyze:
- Kitchen profitability
- Revenue trends
- Operational efficiency
- Variance impact on EBITDA
- Revenue cohort behavior

---

# Tools & Technologies Used

| Category | Tools |
|---|---|
| Programming | Python |
| Data Analysis | Pandas |
| Visualization | Plotly |
| Dashboarding | Streamlit |
| Notebook Environment | Jupyter Notebook |
| IDE | VS Code |

---

# Project Workflow

## 1. Data Cleaning & Preprocessing

Data cleaning was performed in Jupyter Notebook.

Key preprocessing steps:
- Fixed column headers
- Standardized date formatting
- Corrected data types
- Created derived metrics
- Structured cohort categories

Additional metrics created:
- GM_PERCENT
- EBITDA_PERCENT
- VARIANCE_PERCENT

---

## 2. Feature Engineering

Business-oriented categories and buckets were created for analysis.

### Revenue Buckets
Revenue was segmented into fixed cohorts using NET_REVENUE ranges.

### Variance Buckets
Variance percentages were grouped into:
- Var <2%
- Var 2-3%
- Var 3-5%

### EBITDA Status
Stores were classified into:
- High Profit
- Moderate Profit
- Low Profit
- Loss Making

---

## 3. Exploratory Data Analysis

EDA was performed to identify:
- Monthly revenue trends
- EBITDA trends
- Top-performing kitchens
- Variance impact on profitability
- Revenue cohort performance
- City-wise operational behavior

---

# Dashboard Development

The cleaned dataset was exported and used inside a Streamlit dashboard application.

Two dashboard sections were developed.

---

## Dashboard 1 — Kitchen Level PNL

### Features
- KPI Cards
- Monthly Revenue Trend
- Monthly EBITDA Trend
- Top Performing Kitchens
- Revenue vs EBITDA Analysis
- Interactive Filters
- Filtered Dataset Preview

### Filters Used
- City
- Month
- Variance Bucket

---

## Dashboard 2 — Variance Level PNL

### Features
- EBITDA % by Variance Bucket
- Revenue Cohort Variance Matrix
- Store Count Matrix
- Business Insights Section

### Objective
This dashboard focuses on understanding how food wastage variance impacts operational profitability.

---

# Performance Optimization

To improve dashboard responsiveness:
- Streamlit caching (`@st.cache_data`) was implemented
- Aggregated visualizations were used
- Large table rendering was reduced using `.head()`

---

# Key Business Insights

- Kitchens with lower variance percentages consistently achieve stronger EBITDA margins.
- Higher revenue kitchens demonstrate better operational efficiency.
- Variance control appears strongly correlated with profitability improvement.
- Significant profitability differences exist across cities and revenue cohorts.

---

# Project Structure

```text
Kitchen-PNL-Analytics/
│
├── README.md
├── Kitchen_PNL_Analysis.ipynb
├── Kittchen PNL Data.xlsx
│
├── dashboard/
│   ├── app.py
│   ├── cleaned_kitchen_pnl.csv
│   └── requirements.txt
│
└── screenshots/

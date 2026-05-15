# Kitchen PNL Analysis & Dashboard

## Project Objective

The objective of this project was to analyze kitchen-level Profit & Loss (PNL) data for a cloud kitchen company and build interactive dashboards to understand operational and financial performance across stores, cities, and revenue cohorts.

The analysis focuses on:
- Revenue trends
- EBITDA performance
- Gross Margin analysis
- Variance (food wastage) analysis
- Kitchen-level profitability
- Revenue cohort comparisons

---

# Tools & Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- Jupyter Notebook
- VS Code

---

# Project Workflow

## Step 1 — Data Understanding

The raw Excel dataset was explored to understand:
- Kitchen/store-level financial metrics
- Revenue and profitability structure
- Variance (food wastage) behavior
- Monthly trends across cities

---

## Step 2 — Data Cleaning & Preprocessing

Data cleaning was performed in Jupyter Notebook:
- Fixed column names
- Standardized date formats
- Removed inconsistencies
- Converted numerical columns into correct data types

Additional calculated metrics were created:
- GM Percentage
- EBITDA Percentage
- Variance Percentage

---

## Step 3 — Feature Engineering

Business-focused cohorts and buckets were created:
- Revenue Buckets
- Variance Buckets
- EBITDA Status Categories

These features were used for dashboard filtering and business analysis.

---

## Step 4 — Exploratory Data Analysis (EDA)

EDA was performed to identify:
- Monthly revenue trends
- EBITDA patterns
- Top-performing kitchens
- Variance impact on profitability
- Revenue cohort behavior

Key insights were documented in the notebook.

---

## Step 5 — Streamlit Dashboard Development

The cleaned dataset was exported as:
- cleaned_kitchen_pnl.csv

The dashboard was developed in VS Code using Streamlit and Plotly.

Two dashboard sections were created:

### Dashboard 1 — Kitchen Level PNL
Includes:
- KPI cards
- Revenue trends
- EBITDA trends
- Top kitchen analysis
- Revenue vs EBITDA analysis
- Interactive filters

### Dashboard 2 — Variance Level PNL
Includes:
- Variance vs EBITDA analysis
- Revenue cohort variance matrix
- Store count matrix
- Business insights section

---

# Performance Optimization

To improve dashboard performance:
- Streamlit caching (`@st.cache_data`) was used
- Large datasets displayed were limited using `.head()`
- Aggregated views were used for chart rendering

---

# Project Structure

```text
Rebel_Foods_Assignment/
│
├── Kitchen_PNL_Analysis.ipynb
│
├── README.md
│
├── Dashboard/
│   ├── app.py
│   ├── cleaned_kitchen_pnl.csv
│   ├── requirements.txt
│
└── Original_Data/
    └── Kittchen PNL Data.xlsx
import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Kitchen PNL Dashboard",
    layout="wide"
)

# Dashboard title
st.title("Kitchen PNL Dashboard")
tab1, tab2 = st.tabs([
    "Kitchen Level PNL",
    "Variance Level PNL"
])

# =========================
# Load Dataset (Cached)
# =========================

@st.cache_data
def load_data():
    return pd.read_csv("cleaned_kitchen_pnl.csv")

df = load_data()

# =========================
# Sidebar Filters
# =========================
with tab1:

    # =========================
    # Sidebar Filters
    # =========================

    st.sidebar.header("Dashboard Filters")

    selected_city = st.sidebar.multiselect(
        "Select City",
        options=df['CITY'].unique(),
        default=df['CITY'].unique()
    )

    selected_month = st.sidebar.multiselect(
        "Select Month",
        options=df['MONTH'].unique(),
        default=df['MONTH'].unique()
    )

    selected_variance = st.sidebar.multiselect(
        "Select Variance Bucket",
        options=df['VARIANCE_BUCKET'].unique(),
        default=df['VARIANCE_BUCKET'].unique()
    )

    # =========================
    # Apply Filters
    # =========================

    filtered_df = df[
        (df['CITY'].isin(selected_city)) &
        (df['MONTH'].isin(selected_month)) &
        (df['VARIANCE_BUCKET'].isin(selected_variance))
    ]

    # =========================
    # KPI Calculations
    # =========================

    total_revenue = filtered_df['NET_REVENUE'].sum()

    total_ebitda = filtered_df['KITCHEN_EBITDA'].sum()

    def format_indian_currency(num):

        if num >= 10000000:
            return f"₹ {num/10000000:.2f} Cr"

        elif num >= 100000:
            return f"₹ {num/100000:.2f} L"

        else:
            return f"₹ {num:,.0f}"

    avg_gm = filtered_df['GM_PERCENT'].mean()

    store_count = filtered_df['STORE'].nunique()

    # =========================
    # KPI Cards
    # =========================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Revenue",
        format_indian_currency(total_revenue)
    )

    col2.metric(
        "Total EBITDA",
        format_indian_currency(total_ebitda)
    )

    col3.metric(
        "Average GM %",
        f"{avg_gm:.2f}%"
    )

    col4.metric(
        "Store Count",
        store_count
    )

    # =========================
    # Filtered Dataset
    # =========================

    st.subheader("Filtered Dataset")

    columns_to_show = [
        'MONTH',
        'CITY',
        'STORE',
        'NET_REVENUE',
        'GROSS_MARGIN',
        'KITCHEN_EBITDA',
        'VARIANCE_BUCKET',
        'EBITDA_STATUS'
        ]

    st.dataframe(
        filtered_df[columns_to_show].head(30)
    )

    # =========================
    # Monthly Revenue Trend
    # =========================

    st.subheader("Monthly Revenue Trend")

    monthly_revenue_chart = filtered_df.groupby(
        'MONTH'
    )['NET_REVENUE'].sum().reset_index()

    fig_revenue = px.line(
        monthly_revenue_chart,
        x='MONTH',
        y='NET_REVENUE',
        markers=True,
        title='Revenue Trend Over Time',
        height=400
    )

    fig_revenue.update_layout(
        font=dict(size=14)
    )

    st.plotly_chart(fig_revenue, use_container_width=True)

    # =========================
    # Monthly EBITDA Trend
    # =========================

    st.subheader("Monthly EBITDA Trend")

    monthly_ebitda_chart = filtered_df.groupby(
        'MONTH'
    )['KITCHEN_EBITDA'].sum().reset_index()

    fig_ebitda = px.line(
        monthly_ebitda_chart,
        x='MONTH',
        y='KITCHEN_EBITDA',
        markers=True,
        title='EBITDA Trend Over Time',
        height=400
    )

    fig_ebitda.update_layout(
        font=dict(size=14)
    )

    st.plotly_chart(fig_ebitda, use_container_width=True)

    # =========================
    # Top 10 Kitchens by EBITDA
    # =========================

    st.subheader("Top 10 Kitchens by EBITDA")

    top_kitchens = filtered_df.groupby(
        'STORE'
    )['KITCHEN_EBITDA'].sum().reset_index()

    top_kitchens = top_kitchens.sort_values(
        by='KITCHEN_EBITDA',
        ascending=False
    ).head(10)

    fig_top_kitchens = px.bar(
        top_kitchens,
        x='STORE',
        y='KITCHEN_EBITDA',
        title='Top Performing Kitchens',
        height=500,
        text_auto=True
    )

    fig_top_kitchens.update_layout(
        font=dict(size=14)
    )

    st.plotly_chart(fig_top_kitchens, use_container_width=True)

    # =========================
    # Revenue vs EBITDA Analysis
    # =========================

    st.subheader("Revenue vs EBITDA Analysis")

    fig_scatter = px.scatter(
        filtered_df,
        x='NET_REVENUE',
        y='KITCHEN_EBITDA',
        color='CITY',
        hover_data=['STORE'],
        title='Revenue vs EBITDA',
        height=500
    )

    fig_scatter.update_layout(
        font=dict(size=14)
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

    with tab2:

        st.header("Variance Level PNL Dashboard")

        # =========================
        # Variance vs EBITDA Analysis
        # =========================

        st.subheader("Average EBITDA % by Variance Bucket")

        variance_analysis = filtered_df.groupby(
            'VARIANCE_BUCKET'
        )['EBITDA_PERCENT'].mean().reset_index()

        fig_variance = px.bar(
            variance_analysis,
            x='VARIANCE_BUCKET',
            y='EBITDA_PERCENT',
            title='Variance Impact on EBITDA',
            height=400,
            text_auto=True
        )

        fig_variance.update_layout(
            font=dict(size=14)
        )

        st.plotly_chart(fig_variance, use_container_width=True)

        # =========================
        # Revenue Cohort Variance Matrix
        # =========================

        st.subheader("Variance % by Revenue Cohort")

        variance_summary = filtered_df.pivot_table(
            values='VARIANCE_PERCENT',
            index='REVENUE_BUCKET',
            columns='MONTH',
            aggfunc='mean'
        )

        st.dataframe(variance_summary)

        # =========================
        # Store Count Matrix
        # =========================

        st.subheader("Store Count by Variance Bucket")

        store_count_summary = filtered_df.pivot_table(
            values='STORE',
            index=['VARIANCE_BUCKET', 'REVENUE_BUCKET'],
            columns='MONTH',
            aggfunc='count'
        )

        st.dataframe(store_count_summary)

        # =========================
        # Business Insights
        # =========================

        st.subheader("Key Business Insights")

        st.markdown("""
    - Kitchens with variance below 2% maintain the highest EBITDA margins.
    - Lower revenue kitchens show relatively higher food wastage percentages.
    - High revenue kitchens demonstrate stronger operational efficiency.
    - Variance control appears strongly correlated with profitability improvement.
    """)
    st.markdown("---")

    st.caption(
        "Kitchen PNL Dashboard | Built using Streamlit & Plotly"
    )
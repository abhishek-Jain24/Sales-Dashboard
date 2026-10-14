import streamlit as st
import pandas as pd
import numpy as np

# Page settings
st.set_page_config(page_title="Sales Dashboard", page_icon="📊")

# Title
st.title("📊 Sales Dashboard")
st.write("Upload your sales CSV to analyze the data.")

# 1. CSV Upload
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:

    # 2. Read data
    df = pd.read_csv(uploaded_file)

    # 3. Data preview
    st.subheader("📋 Data Preview")
    st.dataframe(df)

    # 4. Summary stats
    st.subheader("📈 Summary")

    total_sales = df["Sales"].sum()
    avg_sales = df["Sales"].mean()
    total_orders = len(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"₹{total_sales}")
    col2.metric("Average Sales", f"₹{avg_sales:.2f}")
    col3.metric("Total Orders", total_orders)

    # 5. Charts
    st.subheader("📊 Sales by Product")
    product_sales = df.groupby("Product")["Sales"].sum()
    st.bar_chart(product_sales)

    st.subheader("📊 Sales by Region")
    region_sales = df.groupby("Region")["Sales"].sum()
    st.bar_chart(region_sales)

    # 6. Filter
    st.subheader("🔍 Filter by Region")
    region = st.selectbox("Select Region", df["Region"].unique())
    filtered = df[df["Region"] == region]
    st.dataframe(filtered)

else:
    st.info("👆 Please upload a CSV file to start.")
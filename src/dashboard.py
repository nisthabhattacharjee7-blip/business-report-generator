import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

from cleaner import clean_data
from analyzer import analyze_df


# page title
st.title("Sales Analytics Dashboard")

# load data 
df = pd.read_csv("data/sales.csv")

# clean data
cleaned_df = clean_data(df)

# sidebar filter 
st.sidebar.header("Filter Data")
selected_category = st.sidebar.selectbox(
    "Select Category",
    cleaned_df['category'].unique()
)
filtered_df = cleaned_df[cleaned_df['category'] == selected_category]

# analyze data
total_revenue, avg_revenue, top_products = analyze_df(filtered_df)

# KPIs
st.header("Business KPIs")

st.metric("Total Revenue", f"${total_revenue:,.2f}")
st.metric("Average Revenue ", f"${avg_revenue:,.2f}")
st.metric("Top Product", top_products)


# show cleaned data
st.header("Cleaned Sales Data")
st.dataframe(filtered_df)

# Revenue by product chart 
st.header("Revenue by Product")

filtered_df['revenue'] =(
    filtered_df['quantity'] *
    filtered_df['price']
)

product_revenue = filtered_df.groupby('product')['revenue'].sum()
fig, ax = plt.subplots()
product_revenue.plot(
    kind='bar', 
    ax=ax
)
st.pyplot(fig)









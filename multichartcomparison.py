import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Multi-Chart Comparison App")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())
    
    # Select columns for comparison
    numerical_columns = df.select_dtypes(include=['number']).columns.tolist()
    selected_columns = st.multiselect("Select columns for comparison", numerical_columns, default=numerical_columns[:2])
    chart_type = st.selectbox("Select chart type", ["Line", "Bar", "Scatter"])
    
    if selected_columns:
        col1, col2 = st.columns(2)
        for i, column in enumerate(selected_columns):
            with (col1 if i % 2 == 0 else col2):
                if chart_type == "Line":
                    fig = px.line(df, y=column, title=f"Line Chart: {column}")
                elif chart_type == "Bar":
                    fig = px.bar(df, y=column, title=f"Bar Chart: {column}")
                else:
                    fig = px.scatter(df, y=column, title=f"Scatter Plot: {column}")
                st.plotly_chart(fig)

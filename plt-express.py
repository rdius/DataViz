import streamlit as st
import plotly.express as px
import pandas as pd

# Create sample data
data = {
    'Age': [22, 25, 47, 52, 46, 56, 55, 38],
    'Income': [35000, 42000, 79000, 85000, 76000, 90000, 94000, 62000]
}
df = pd.DataFrame(data)

# Sidebar for filtering data
st.sidebar.header("Filter Options")
min_age = st.sidebar.slider("Minimum Age", int(df['Age'].min()), int(df['Age'].max()), int(df['Age'].min()))
max_age = st.sidebar.slider("Maximum Age", int(df['Age'].min()), int(df['Age'].max()), int(df['Age'].max()))

# Filter data based on user input
filtered_df = df[(df['Age'] >= min_age) & (df['Age'] <= max_age)]

# Display the filtered scatter plot using Plotly
fig = px.scatter(filtered_df, x='Age', y='Income', title="Filtered Age vs Income")
st.plotly_chart(fig)

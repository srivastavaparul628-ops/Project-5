import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Telecom Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("final_df.csv")

df = load_data()

st.title("📊 Telecom User Analytics Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Users", len(df))
col2.metric("Avg Engagement", round(df['engagement_score'].mean(),2))
col3.metric("Avg Satisfaction", round(df['satisfaction_score'].mean(),2))

# Scatter plot
st.subheader("Engagement vs Experience")
fig, ax = plt.subplots()
sns.scatterplot(
    x=df['engagement_score'],
    y=df['experience_score'],
    hue=df['satisfaction_score'],
    ax=ax
)
st.pyplot(fig)

# Top users
st.subheader("Top 10 Users")
st.dataframe(df.nlargest(10, 'satisfaction_score'))
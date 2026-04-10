
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

st.subheader("Top 10 Satisfied Users")
st.write(df.nlargest(10, 'satisfaction_score'))

st.subheader("Engagement vs Experience")
fig, ax = plt.subplots()
sns.scatterplot(x=df['engagement_score'], y=df['experience_score'], hue=df['satisfaction_cluster'], ax=ax)
st.pyplot(fig)

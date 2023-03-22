import streamlit as st 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

names_link = 'dataset.csv'
names_data = pd.read_csv(names_link)
st.title ("Read CSV")

st.dataframe(names_data)

fig, ax = plt.subplots()

sns.countplot(x=names_data.sex, ax=ax)

st.pyplot(fig)
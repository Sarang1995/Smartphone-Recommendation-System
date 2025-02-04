import streamlit as st
import pandas as pd
import requests

st.title("Smartphone Recommendation SYstem")

st.write("Smartphone Recommendation System using multiple recommendation techniques, ensuring personalized and relevant suggestions for users.")

cosine_df = pd.read_csv("cosine_df.csv")

tab1, tab2, tab3, tab4 = st.tabs(['Content-Based Filtering','Knowledge Based Filtering', 'Utility Based Filtering', "Hybrid Model"])

with tab1:
    st.write("Cosine similarity is a popular metric used to measure the similarity between two non-zero vectors in a multi-dimensional space. It calculates the cosine of the angle between two vectors, which indicates how similar the vectors are in terms of their direction.")
    
    name = st.selectbox("Select the Smartphone", cosine_df['model'].unique().tolist())

    rec = (cosine_df[['model', name]].sort_values(by=name, ascending=False)
    .head(10).reset_index())

    rec = rec.iloc[:, 1]

    st.dataframe(rec)

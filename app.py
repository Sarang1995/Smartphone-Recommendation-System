import streamlit as st
import pandas as pd
import requests

st.title("Smartphone Recommendation SYstem")

st.write("Smartphone Recommendation System using multiple recommendation techniques, ensuring personalized and relevant suggestions for users.")

# cosine_df = pd.read_csv("cosine_df.csv")

# tab1, tab2, tab3, tab4 = st.tabs(['Content-Based Filtering','Knowledge Based Filtering', 'Utility Based Filtering', "Hybrid Model"])

# with tab1:
#     st.write("Cosine similarity is a popular metric used to measure the similarity between two non-zero vectors in a multi-dimensional space. It calculates the cosine of the angle between two vectors, which indicates how similar the vectors are in terms of their direction.")
    
#     name = st.selectbox("Select the Smartphone", cosine_df['model'].unique().tolist())

#     rec = (cosine_df[['model', name]].sort_values(by=name, ascending=False)
#     .head(10).reset_index())

#     rec = rec.iloc[:, 1]

#     st.dataframe(rec, width=True)

UNSPLASH_ACCESS_KEY = "AM8uTx4EE8Lv4rMSg73BUTkzAsT7KEfNCbhGrQLmj88"

def get_mobile_image(mobile_name):
    url = f"https://api.unsplash.com/search/photos?query={mobile_name}&client_id={UNSPLASH_ACCESS_KEY}"
    response = requests.get(url).json()

    if "results" in response and len(response["results"]) > 0:
        return response["results"][0]["urls"]["regular"]
    else:
        return None

mobile_name = "iPhone 14"
image_url = get_mobile_image(mobile_name)

if image_url:
    st.image(image_url, caption=mobile_name, use_column_width=True)
else:
    st.error("No image found!")

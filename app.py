import streamlit as st
import pandas as pd

st.title("Smartphone Recommendation SYstem")

st.write("Smartphone Recommendation System using multiple recommendation techniques, ensuring personalized and relevant suggestions for users.")

cosine_df = pd.read_csv("cosine_df.csv")
df = pd.read_csv('know_df.csv')
utility_df = pd.read_csv("utility_df.csv")
items = pd.read_csv("items.csv")

tab1, tab2, tab3, tab4 = st.tabs(['Content-Based Filtering','Knowledge Based Filtering', 'Utility Based Filtering', "Hybrid Model"])

with tab1:
    st.write("Cosine similarity is a popular metric used to measure the similarity between two non-zero vectors in a multi-dimensional space. It calculates the cosine of the angle between two vectors, which indicates how similar the vectors are in terms of their direction.")
    
    name = st.selectbox("Select the Smartphone", cosine_df['model'].unique().tolist(), key="tab1_select")

    rec = (cosine_df[['model', name]].sort_values(by=name, ascending=False)
    .reset_index())

    recs = rec.iloc[:, 1]

    st.dataframe(recs.head(10))

with tab2:

    st.subheader("Knowledge based recommender system by taking smartphone name from user")
    st.write("When user select the Smartphone, model will compare selected smartphone's attributes to all and give the best Smartphones recommendations")

    name = st.selectbox("Select your Smartphone", df['model'].unique().tolist())

    price = df.loc[df['model'] == name]['price'].values[0]
    ram_capacity = df.loc[df['model'] == name]['ram_capacity'].values[0]
    internal_memory = df.loc[df['model'] == name]['internal_memory'].values[0]
    primary_camera_rear = df.loc[df['model'] == name]['primary_camera_rear'].values[0]
    primary_camera_front = df.loc[df['model'] == name]['primary_camera_front'].values[0]
    
    
    data = df[
            (df['price'] >= price) &
            (df['ram_capacity'] >= ram_capacity) &
            (df['internal_memory'] >= internal_memory) &
            (df['primary_camera_rear'] >= primary_camera_rear) &
            (df['primary_camera_front'] >= primary_camera_front)]
    
    data = data.sort_values(['price','ram_capacity','internal_memory','primary_camera_rear','primary_camera_front'],
                                         ascending=[True, True, True, True, True]).head(10).reset_index()

    data = data.iloc[:, 2:]
    
    if st.button("Recommend"):
        st.dataframe(data)



    st.subheader("Knowledge based recommender system by taking inputs from user")
    st.write("According to the users' inputs, we will recommend them the best Smartphones")

    price_min = st.number_input('Enter the minimum price:', step=100, format='%d')
    price_max = st.number_input('Enter the maximum price:', step=100, format='%d')
    ram_capacity = st.number_input('Enter the require RAM capacity in GB:', step=1, format='%d')
    internal_memory = st.number_input('Enter the require intenla memory in GB:', step=1, format='%d')
    primary_camera_rear = st.number_input('Enter the require back camera in MP:', step=1, format='%d') 
    primary_camera_front = st.number_input('Enter the require front camers in MP:', step=1, format='%d')
               
    ## Filtering data
    filtered_df = df[
                    (df['price'] >= price_min) &
                    (df['price'] <= price_max) &
                    (df['ram_capacity'] >= ram_capacity) &
                    (df['internal_memory'] >= internal_memory) &
                    (df['primary_camera_rear'] >= primary_camera_rear) &
                    (df['primary_camera_front'] >= primary_camera_front)]
        
    filtered_df = filtered_df.sort_values(['price','ram_capacity','internal_memory','primary_camera_rear','primary_camera_front'],
                                            ascending=[True, True, True, True, True]).head(10).reset_index()
        
    filtered_df = filtered_df.iloc[:, 2:]
    
    if st.button("Recommend Smartphones"):
        st.dataframe(filtered_df)


with tab3:

    st.header("Utility-Based Recommender System")

    st.write("A utility-based recommender system makes recommendations by predicting the 'utility' (usefulness or satisfaction) a user would derive from a product. The utility is typically represented as a numerical score derived from the product's attributes.")

    price_weight = st.number_input("Enter weight for price (0 to 1):", step=0.01, format='%.2f')
    rating_weight = st.number_input("Enter weight for rating (0 to 1):", step=0.01, format='%.2f')
    battery_weight = st.number_input("Enter weight for battery (0 to 1):", step=0.01, format='%.2f')
    ram_weight = st.number_input("Enter weight for RAM (0 to 1):", step=0.01, format='%.2f')
    memory_weight = st.number_input("Enter weight for memory (0 to 1):", step=0.01, format='%.2f')
    back_camera_weight = st.number_input("Enter weight for back camera (0 to 1):", step=0.01, format='%.2f')
    front_camera_weight = st.number_input("Enter weight for front camera (0 to 1):", step=0.01, format='%.2f')
    
    weights = {'price':price_weight,
              'avg_rating':rating_weight,
              'battery_capacity':battery_weight,
              'ram_capacity':ram_weight,
              'internal_memory':memory_weight,
              'primary_camera_rear':back_camera_weight,
              'primary_camera_front':front_camera_weight}
    
    ## Calculate utility scores
    utility_df['utility_score'] = sum(utility_df[col] * weights[col] for col in weights)
    
    ## Sort the utility score
    utility_df = utility_df.sort_values(by='utility_score', ascending=False).head(10).reset_index()

    utility_df = utility_df.iloc[:,2]

    if st.button("Recommend utility based Smartphones"):
        st.dataframe(utility_df)


with tab4:

    st.title("Hybrid Model")

    st.write("A Hybrid Recommender System combines different recommendation techniques to provide better recommendations by leveraging the strengths of each. In our case, we will combine **Content-Based Filtering** and **Knowledge-Based Filtering**.")

    
    name_model = st.selectbox("Select the Smartphone", cosine_df['model'].unique().tolist(), key="tab4_select")

    rec_model = (cosine_df[['model', name_model]].sort_values(by=name_model, ascending=False)
    .reset_index())

    rec_model = rec_model.iloc[:, 1]

    # st.dataframe(rec_model.head(10))
    
    
    hybrid_df = rec.merge(df, left_on="model", right_on="model")

    # st.dataframe(hybrid_df)

    cols = ['model','price', 'ram_capacity','internal_memory','primary_camera_rear','primary_camera_front']
    hybrid_df = hybrid_df.loc[:, hybrid_df.columns.isin(cols)]
    # st.dataframe(hybrid_df)



    price = hybrid_df.loc[hybrid_df['model'] == name_model]['price'].values[0]
    ram_capacity = hybrid_df.loc[hybrid_df['model'] == name_model]['ram_capacity'].values[0]
    internal_memory = hybrid_df.loc[hybrid_df['model'] == name_model]['internal_memory'].values[0]
    primary_camera_rear = hybrid_df.loc[hybrid_df['model'] == name_model]['primary_camera_rear'].values[0]
    primary_camera_front = hybrid_df.loc[hybrid_df['model'] == name_model]['primary_camera_front'].values[0]
    
    
    hybrid = hybrid_df[
            (hybrid_df['price'] >= price) &
            (hybrid_df['ram_capacity'] >= ram_capacity) &
            (hybrid_df['internal_memory'] >= internal_memory) &
            (hybrid_df['primary_camera_rear'] >= primary_camera_rear) &
            (hybrid_df['primary_camera_front'] >= primary_camera_front)]

    # st.dataframe(hybrid)
    
    hybrid_data = hybrid.sort_values(['price','ram_capacity','internal_memory','primary_camera_rear','primary_camera_front'],
                                         ascending=[True, True, True, True, True]).head(10).reset_index()
    # st.dataframe(hybrid_data)

    hybrid_data = hybrid_data.iloc[:, 1:]
    
    if st.button("Recommendations"):
        st.dataframe(hybrid_data)






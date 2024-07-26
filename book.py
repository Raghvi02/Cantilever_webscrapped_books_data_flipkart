import streamlit as st
import pandas as pd
st.title('Book Filter App')
df= pd.read_csv('WEB_BOOKS')
price_options = ['Less than 500', '500-1000', 'More than 1000']
selected_price_option = st.selectbox('Select Price Range', price_options)

# Dropdown for Rating
rating_options = sorted(df['Rating'].unique())
selected_rating = st.selectbox('Select Rating', rating_options)

# Filter DataFrame based on selected price range
if selected_price_option == 'Less than 500':
    filtered_df = df[df['Price'] < 500]
elif selected_price_option == '500-1000':
    filtered_df = df[(df['Price'] >= 500) & (df['Price'] <= 1000)]
elif selected_price_option == 'More than 1000':
    filtered_df = df[df['Price'] > 1000]

# Further filter DataFrame based on selected rating
filtered_df = filtered_df[filtered_df['Rating'] == selected_rating]
st.dataframe(filtered_df)
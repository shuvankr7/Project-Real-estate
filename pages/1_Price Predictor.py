import streamlit as st
import pickle
import pandas as pd
import numpy as np
from huggingface_hub import hf_hub_download

# Set page config FIRST
st.set_page_config(page_title="Viz Demo")

# Download model pipeline from HuggingFace
@st.cache_resource
def load_pipeline():
    pipeline_path = hf_hub_download(repo_id="shuvankar777/real", filename="pipeline.pkl")
    with open(pipeline_path, 'rb') as file:
        return pickle.load(file)

# Load local dataframe
@st.cache_resource
def load_df():
    with open('df.pkl', 'rb') as file:
        return pickle.load(file)

pipeline = load_pipeline()
df = load_df()

# UI Inputs
st.header('Enter your inputs')

property_type = st.selectbox('Property Type', ['flat', 'house'])
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
bedrooms = float(st.selectbox('Number of Bedroom', sorted(df['bedRoom'].unique().tolist())))
bathroom = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))
balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))
property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))
built_up_area = float(st.number_input('Built Up Area'))
servant_room = float(st.selectbox('Servant Room', [0.0, 1.0]))
store_room = float(st.selectbox('Store Room', [0.0, 1.0]))
furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

# Prediction
if st.button('Predict'):
    data = [[
        property_type, sector, bedrooms, bathroom, balcony,
        property_age, built_up_area, servant_room, store_room,
        furnishing_type, luxury_category, floor_category
    ]]
    columns = [
        'property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
        'agePossession', 'built_up_area', 'servant room', 'store room',
        'furnishing_type', 'luxury_category', 'floor_category'
    ]
    input_df = pd.DataFrame(data, columns=columns)

    base_price = np.expm1(pipeline.predict(input_df))[0]
    low, high = base_price - 0.22, base_price + 0.22

    st.success(f"💰 Estimated price: ₹{round(low, 2)} Cr to ₹{round(high, 2)} Cr")

# Footer
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background-color: #f1f1f1;
            color: black;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        <p>© 2025 Shuvankar Naskar | Powered by Streamlit 🚀</p>
        <p>
            <a href="https://www.linkedin.com/in/shuvankar-naskar-data-scientist" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20"/>
                Connect on LinkedIn
            </a>
        </p>
    </div>
""", unsafe_allow_html=True)

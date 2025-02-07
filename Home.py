import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
)

st.header("Habibi Welcome to Gurgaon! 👋")

st.write(''' Here we have 3 section
             1. Price Predictor - Here user can input 12 parameters and according to that parameter predicted flat price range will be shown
             2. Analysis App - Here you will be visualizing different analysis
             3. Recommend Appartments - Model will recommend you top 5 appartments based on your inputs''')

st.sidebar.success("Select a demo above.")

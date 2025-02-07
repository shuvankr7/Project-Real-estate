import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
)

st.header("Habibi Welcome to Gurgaon! 👋")

st.write(''' Here we have 3 section - \n1. Price Predictor - Here user can input 12 parameters and according to that parameter predicted flat price range will be shown\n2. Analysis App - Here you will be visualizing different analysis\n3. Recommend Appartments - Model will recommend you top 5 appartments based on your inputs''')
st.write('\n')
st.write('Please note - This model is build on data of gurgaon only')
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
        <p>© 2024 Shuvankar Naskar | Powered by Streamlit 🚀</p>
    </div>
""", unsafe_allow_html=True)
st.sidebar.success("Select a demo above.")

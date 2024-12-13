import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

st.set_page_config(page_title='Data Preprocessing',
                   layout='centered',
                   initial_sidebar_state='expanded',
)

tab1, tab2 = st.tabs(["Data visualisation", "Data Cleaning"])

@st.cache_data
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df
# Load the data and store it in session_state
try:
    if "data" not in st.session_state:
        data_filepath = r'C:\Users\Soso\Desktop\ML_miniprojet\ML_mini_projet\app\data\Groceries_dataset2.csv'
        st.session_state.data = load_data(data_filepath)
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Use the data in this page
df = st.session_state.data
# Sidebar Components
st.sidebar.header("Visualization Data Settings")

with tab1:
    st.dataframe(df)
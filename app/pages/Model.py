import streamlit as st
import pandas as pd
import pickle
from mlxtend.frequent_patterns import association_rules
import os



st.set_page_config(page_title='Data Preprocessing',
                   layout='centered',
                   initial_sidebar_state='expanded',
)

tab1, tab2 = st.tabs(["Model rules", "Reommanded System"])
#----------------------------------------------------------------------------------------------------------------------------------------

#load train data
def load_csv_data(path):
        try:
            df = pd.read_csv(path)
            return df
        except FileNotFoundError:
            st.error("Error: dataset not found. Please ensure the file is present in the 'data' folder.")
            return None 
st.session_state.train_data = load_csv_data("data\\train_data.csv")

items_list = st.session_state.data.columns.tolist()
current_dir = os.path.dirname(__file__)

with tab1 :
    # App title
    st.title("FP-Growth - Frequent Itemsets and Association Rules")
    #----------------------------------------------------------------------------------------------------------------------------------------
    #side bar
    st.sidebar.header('User Input Features')

    st.sidebar.markdown("""
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
    """)

    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

    # Sidebar for parameters
    st.sidebar.header("Parameters")
    min_support = st.sidebar.slider("Minimum Support", 0.01, 0.5, 0.05)
    min_confidence = st.sidebar.slider("Minimum Confidence", 0.01, 1.0, 0.07)
    #----------------------------------------------------------------------------------------------------------------------------------------
    # Load the model
    @st.cache_data
    def load_model(path):
        model = pickle.load(open(path, 'rb'))
        return model

    model_filepath = os.path.join(current_dir, '..', 'data', 'model.pkl')
    FPgrowth_model = load_model(model_filepath)
    # FPgrowth_model = load_model("data\\model.pkl")

    frequent_itemsets = FPgrowth_model[FPgrowth_model['support'] >= min_support]

    st.write("### Frequent Itemsets")
    if not frequent_itemsets.empty:
        st.write(frequent_itemsets)
    else:
        st.write("No frequent itemsets found with the selected support threshold.")
    if not frequent_itemsets.empty:
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence,num_itemsets=2)
        st.write("### Association Rules")
        if not rules.empty:
            st.write(rules)
            st.markdown(f' ## Number of generated rules is: :orange[{rules.shape[0]}]')

        else:
            st.write("No rules found with the selected confidence threshold.")
    else:
        st.write("Unable to generate rules as no frequent itemsets were found.")

with tab2 :
    #item list user inputs
    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
        st.write(input_df)
    else:

        options = st.multiselect('Choose an item :' , items_list)
        recommendations = []
        options.sort()

        # st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    
    #---------------------------------------------------------------------------------------------------------------------------------
    # Load the model
    #make a prediction
    st.subheader('Predictions')
    if options:
        user_transaction = frozenset(options)
        applicable_rules = rules[rules['antecedents'] == user_transaction]
        recommendations = applicable_rules['consequents'].tolist()
    else:
        st.write("Select items to see recommendations.")

    # Recommend items from the consequents
    st.markdown(
        """
        <style>
        .stButton > button {
            background-color: green;
            color: white;
            border: none;
            padding: 0.4rem 1rem;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
        )
    if st.button("Predict"):
        st.write("Recommended items:", recommendations)



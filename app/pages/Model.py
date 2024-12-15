import streamlit as st
import pandas as pd
import pickle
from mlxtend.frequent_patterns import association_rules ,fpgrowth
import os
import seaborn as sns
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 


st.set_page_config(page_title='Data Preprocessing',
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='expanded',
)

tab1, tab2 = st.tabs(["Model rules", "Reommanded System"])

current_dir = os.path.dirname(__file__)
#----------------------------------------------------------------------------------------------------------------------------------------

#load train data
def load_csv_data(path):
        try:
            df = pd.read_csv(path)
            return df
        except FileNotFoundError:
            st.error("Error: dataset not found. Please ensure the file is present in the 'data' folder.")
            return None 

        

data_filepath = os.path.join(current_dir, '..', 'data', 'train_data.csv')    
st.session_state.train_data = load_csv_data(data_filepath)


items_list = st.session_state.train_data.columns.tolist()



with tab1 :
    # App title
    st.title("FP-Growth - Frequent Itemsets and Association Rules")
    #----------------------------------------------------------------------------------------------------------------------------------------
    #side bar
    st.sidebar.header('User Input Features')

    st.sidebar.markdown("""
    [Example CSV input file](data/test.csv)
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


    # if uploaded_file is not None:
    #     try:
    #         input_df = pd.read_csv(uploaded_file)
    #         if input_df.empty:
    #             st.error("Uploaded file is empty. Please upload a file with data.")
    #         else:
    #             st.write("Data loaded successfully")
    #             st.write(input_df)
    #     except pd.errors.EmptyDataError:
    #         st.error("The uploaded file is empty or has no data.")
    #     except Exception as e:
    #         st.error(f"Error loading file: {e}")
    # else:
    #     st.warning("Please upload a CSV file to start processing.")


    if uploaded_file is not None:
        try:
            # Read the uploaded CSV file into a DataFrame
            input_df = pd.read_csv(uploaded_file,encoding='utf-8', delimiter=',')

            # Check if the dataframe is empty
            if input_df.empty:
                st.error("Uploaded file is empty. Please upload a file with data.")
            else:
                st.write("Data loaded successfully:")
                st.write(input_df)

                # Now pass the dataframe to the fpgrowth function
                frequent_itemsets = fpgrowth(input_df, min_support=min_support, use_colnames=True)
                rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence,num_itemsets=2)
                st.session_state.rules = rules
                # # Display the frequent itemsets
                # st.write("Frequent Itemsets:")
                # st.write(frequent_itemsets)

                # # Generate association rules
                # rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=min_confidence, num_itemsets=2)
                # st.write("Association Rules:")
                # st.write(rules)

        except pd.errors.EmptyDataError:
            st.error("The uploaded file is empty or has no data.")
        except Exception as e:
            st.error(f"Error loading file: {e}")
    else:
        # st.warning("Please upload a CSV file to start processing.")
            model_filepath = os.path.join(current_dir, '..', 'data', 'model.pkl')
            FPgrowth_model = load_model(model_filepath)
            frequent_itemsets = FPgrowth_model[FPgrowth_model['support'] >= min_support]
            rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence,num_itemsets=2)
            st.session_state.rules = rules

    if st.button("show rules"):
        st.write("### Frequent Itemsets")
        if not frequent_itemsets.empty:
            st.write(frequent_itemsets)
        else:
            st.write("No frequent itemsets found with the selected support threshold.")
        if not frequent_itemsets.empty:
            rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence,num_itemsets=2)
            st.session_state.rules = rules
            st.write("### Association Rules")
            if not rules.empty:
                st.write(rules)
                st.markdown(f' ## Number of generated rules is: :orange[{rules.shape[0]}]')

            else:
                st.write("No rules found with the selected confidence threshold.")
        else:
            st.write("Unable to generate rules as no frequent itemsets were found.")
    #-----------------------------------------------------------------------------------------------


        # Scatter plot of support vs confidence
        st.subheader('Support vs Confidence Scatter Plot')
        support = rules['support'].to_numpy()
        confidence = rules['confidence'].to_numpy()

        plt.figure(figsize=(8, 6))
        plt.scatter(support, confidence, alpha=0.5, marker="*")
        plt.title('Support vs Confidence')
        plt.xlabel('Support')
        plt.ylabel('Confidence')
        st.pyplot(plt)


        # Draw graph
        def draw_graph(rules, rules_to_show):
            G = nx.DiGraph()  # Create a directed graph
            colors = np.random.rand(len(rules))
            color_map = []
            node_labels = {}

            # Build the graph with rules
            for i in range(min(rules_to_show, len(rules))):
                rule_id = f"R{i}"
                G.add_node(rule_id)  # Add a node for the rule
                node_labels[rule_id] = f"Rule {i+1}"

                # Add edges from antecedents to the rule
                for antecedent in rules.iloc[i]['antecedents']:
                    G.add_node(antecedent)
                    G.add_edge(antecedent, rule_id, color=colors[i], weight=2)

                # Add edges from the rule to consequents
                for consequent in rules.iloc[i]['consequents']:
                    G.add_node(consequent)
                    G.add_edge(rule_id, consequent, color=colors[i], weight=2)

            # Extract edge attributes for drawing
            edges = G.edges()
            edge_colors = [G[u][v]['color'] for u, v in edges]
            edge_weights = [G[u][v]['weight'] for u, v in edges]

            # Draw the graph
            pos = nx.spring_layout(G, k=16, scale=1)  # Layout for nodes
            nx.draw(G, pos, edge_color=edge_colors, width=edge_weights, with_labels=False,
                    node_color="lightblue", node_size=2000)
            nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10)
            # plt.show()
            st.pyplot(plt)  # Display the graph in Streamlit

            # draw_graph(rules, 6)

        st.subheader('Association Rules Graph')
        # Slider to control the number of rules to display in the graph
        # rules_to_show = st.slider('Number of Rules to Show in Graph', 1, len(rules), 6)
        # Display graph
        fig = draw_graph(rules, 10)
        # st.pyplot(fig)
        # draw_graph(rules, rules_to_show)
        #-----------------------------------------------------------------------------------------------


with tab2 :
    #item list user inputs
    # if uploaded_file is not None:
        # input_df = pd.read_csv(uploaded_file,encoding='utf-8', delimiter=',')
        # st.write(input_df)
    # else:

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
    if st.button("Recommend"):
        # st.write("Recommended items:", recommendations)

         # Display the recommendations as a bullet list
        # for idx, item in enumerate(recommendations):
        #     item_str = ', '.join(list(item))
        #     st.markdown(f"- {item_str}")

        # Convert the frozensets into a list of strings
        item_strings = [', '.join(list(item)) for item in recommendations]
        # Create a DataFrame to display as a table
        st.markdown(f' ## Number of Recommended Items is: :orange[{len(recommendations)}]')
        df = pd.DataFrame(item_strings, columns=["Recommended Items"])
        # Display the DataFrame in Streamlit
        st.markdown("### Recommended Items Table:")
        st.table(df)

        # Display the recommendations with checkboxes
        # st.markdown("### Recommended Items with Checkboxes:")
        # for idx, item in enumerate(recommendations):
        #     item_str = ', '.join(list(item))
        #     if st.checkbox(f"Select {item_str}", key=idx):
        #         st.write(f"You selected: {item_str}")



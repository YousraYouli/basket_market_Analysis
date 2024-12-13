import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from wordcloud import WordCloud
from mlxtend.preprocessing import TransactionEncoder

# import matplotlib.pyplot as plt
import path

dir = path.Path(__file__).abspath()
sys.append.path(dir.parent.parent)


st.set_page_config(page_title='Data Preprocessing',
                   layout='centered',
                   initial_sidebar_state='expanded',
)

tab1, tab2 = st.tabs(["Data visualisation", "Data Cleaning"])

@st.cache_data
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

# Charger les données et les stocker dans session_state
try:
    if "data" not in st.session_state:
<<<<<<< HEAD
        data_filepath = r'C:\Users\Soso\Desktop\ML_miniprojet\ML_mini_projet\app\data\Groceries_dataset2.csv'
        # data_filepath = os.path.join('.', 'Groceries_dataset2.csv')
=======
        data_filepath = os.path.join('.', 'data', 'Groceries_dataset2.csv')
>>>>>>> 36816ba9f4d7acc92a8c71e448ec8ec7142730e7
        st.session_state.data = load_data(data_filepath)
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Utiliser les données sur cette page
data = st.session_state.data

# Sidebar Components
st.sidebar.header("Visualization Data Settings")

with tab1:
    st.header("Data Visualisation")
    st.dataframe(data)

    # Afficher les informations sur les données
    st.subheader("Dataset Information")
    st.text(data.info(buf=None))
    st.write(data.describe())
    st.write("Data Types:")
    st.write(data.dtypes)
    st.write("Shape of Data:")
    st.write(data.shape)

    # Visualisation des articles les plus fréquents
    st.subheader("Top 10 Most Popular Items")
    item_counts = data['itemDescription'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(item_counts.index[:10], item_counts.values[:10])
    ax.set_xlabel('Item Description')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Most Popular Items')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Afficher les valeurs nulles
    st.subheader("Missing Values")
    st.write(data.isnull().sum())

    # Heatmap des valeurs nulles
    warnings.filterwarnings('ignore')
    st.subheader("Missing Values Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(data.isnull(), cmap='viridis', ax=ax, cbar=False)
    ax.set_title("Missing Values Heatmap")
    ax.axis("off")
    st.pyplot(fig)

with tab2:
    st.header("Data Cleaning")

    # Supprimer les lignes avec des valeurs manquantes
    st.subheader("Handling Missing Values")
    st.write(f"Lignes restantes avant suppression des valeurs manquantes : {len(data)}")
    data2 = data.dropna()
    st.write(f"Lignes restantes après suppression des valeurs manquantes : {len(data2)}")

    # Nettoyer les colonnes textuelles (tous en minuscule)
    st.subheader("Text Cleaning")
    data2['itemDescription'] = data2['itemDescription'].str.lower().str.strip()
    st.write("Exemple de descriptions après nettoyage :")
    st.write(data2['itemDescription'].head())

    # Supprimer les doublons
    st.subheader("Removing Duplicates")
    st.write(f"Lignes restantes avant suppression des doublons : {len(data2)}")
    data3 = data2.drop_duplicates()
    st.write(f"Lignes restantes après suppression des doublons : {len(data3)}")

    # Enregistrer les données nettoyées dans un fichier CSV
    st.subheader("Save Cleaned Data")
    cleaned_file_path = "Cleaned_Groceries_dataset.csv"
    data3.to_csv(cleaned_file_path, index=False)
    st.write(f"Données nettoyées enregistrées dans : {cleaned_file_path}")

    # Word Cloud
    st.subheader("Word Cloud")
    text = " ".join(review for review in data3['itemDescription'])
    wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate(text)
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.set_title("Word Cloud of Items")
    ax.axis("off")
    st.pyplot(fig)

    # Prétraitement: Grouper les articles par chaque transaction
    st.subheader("Grouped Transactions")
    transactions = data3.groupby('Member_number')['itemDescription'].apply(list)
    st.write(transactions)

    # Convertir les transactions au format One-Hot Encoding
    st.subheader("One-Hot Encoding of Transactions")
    te = TransactionEncoder()
    te_array = te.fit(transactions).transform(transactions)
    df_encoded = pd.DataFrame(te_array, columns=te.columns_)
    st.write("Shape of Encoded Data:")
    st.write(df_encoded.shape)
    st.dataframe(df_encoded)

import streamlit as st
import os 

st.set_page_config(page_title='home',
                   page_icon='👋',
                   layout='wide',
                   initial_sidebar_state='expanded',
                   menu_items={
                       'Get Help':'https://github.com/YousraYouli/Association_Rule_Mining/tree/main/pages',
                       'About':'#welcome to the ML mini projet'
                   }
)

st.title('welcome to association model')
st.subheader("""This is unsupervised algorithm to find hide patterns and relations between items we will be :green[Preparing Data] to train an :green[Apriori Model] to create a :green[Basket Market Analysis and item list Recommendation System]
             """)
st.markdown("""
    ### you can find the data in the link below
    - Check out [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset?resource=download&select=Books.csv)
    - credits for the team : 
            MEFLAH Yousra
            OUECHENE Hiba
            BELHOUARI Noussaiba

"""
)
# st.title('problematique ?')
# st.title('solution : Association Rule Mining algorithm')
# st.write(' arm is (support, confidence , lift)....etc')
# st.write('''we have test the three algorithm of **Association Rule Mining** wich are 
#          :blue[Apriori ,FP-GROWTH, ECLAT] and we had a diffrenet result , the best model
#          using blue:[performance evaluation] is **XXX algorihtm** ''')

# data_filepath = os.path.join('.', 'figures','1.png')
# st.image(data_filepath)
st.image("ML_mini_projet\app\figures\1.png")

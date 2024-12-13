import streamlit as st
<<<<<<< HEAD
# import os 
=======
import os 
>>>>>>> 36816ba9f4d7acc92a8c71e448ec8ec7142730e7

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
st.markdown (""" #### This is unsupervised algorithm to find hide patterns and relations between items we will be :green[Preparing Data] to train an :green[FP-GROWTH Model] to create a :green[Basket Market Analysis and item list Recommendation System]
             """)
st.markdown(''' ####  we have tested the three algorithm of **Association Rule Mining** wich are :green[Apriori ,FP-GROWTH, ECLAT] and we had a diffrenet result , the best model using :green[performance evaluation] is :orange[FP-GROWTH algorihtm] 
             ''')
st.markdown("""
     you can find the data in the link : [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset?resource=download&select=Books.csv) <br>
    credits for the team : <br>
            - MEFLAH Yousra <br>
            - OUECHENE Hiba <br>
            - BELHOUARI Noussaiba

""", unsafe_allow_html=True
)

<<<<<<< HEAD


# data_filepath = os.path.join('.', 'figures','1.png')
st.image(r'C:\Users\Soso\Desktop\ML_miniprojet\ML_mini_projet\app\figures\1.png')
=======
data_filepath = os.path.join('.', 'figures','1.png')
st.image(data_filepath)
# st.image("C:\Users\Soso\Desktop\ML_miniprojet\ML_mini_projet\app\figures1.png")
>>>>>>> 36816ba9f4d7acc92a8c71e448ec8ec7142730e7

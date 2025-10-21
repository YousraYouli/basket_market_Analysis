# ML_mini_projet : Association_Rule_Mining on basket market dataset 

## 🎯 Project Overview
This **mini machine learning project** was developed as part of a **university assignment**.  
It focuses on discovering **association rules** in a **market basket dataset** using three algorithms:
- **Apriori**
- **Eclat**
- **FP-Growth**

After comparing their performance, the **FP-Growth algorithm** was selected and deployed through a **Streamlit web app** for interactive rule exploration.

## 🧠 Objective
To identify frequent product combinations and generate strong association rules from customer transaction data, helping understand **shopping patterns**.

## 🧪 Algorithms Compared
| Algorithm | Description | Result |
|------------|-------------|---------|
| **Apriori** | Traditional algorithm for frequent itemset mining | Accurate but slower |
| **Eclat** | Uses intersection-based approach | Faster than Apriori |
| **FP-Growth** | Builds a compact FP-tree for mining | ⚡ Best performance (used for deployment) |

## 🧰 Technologies Used
- Python 
- Pandas / NumPy  
- mlxtend (for Apriori, Eclat, FP-Growth)  
- Streamlit  
- Scikit-learn  
- Matplotlib / Seaborn (for visualization)

## ⚙️ How to Run Locally
1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ML_mini_projet.git
   cd ML_mini_projet

2. **use virtual environement**
  ```bash
   python -m venv venv
````
3. **install the required dependencies using**
 ```bash
  pip install -r requirements.txt
  pip install streamlit
  streamlit run home.py
````
📊 you can find dataSet here : 
https://www.kaggle.com/datasets/heeraldedhia/groceries-dataset

🌐 you can test the model from here : https://mlminiprojet.streamlit.app/

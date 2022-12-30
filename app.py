import streamlit as st
import base64
import sklearn
import numpy as np
import pickle as pkl
from sklearn.preprocessing import MinMaxScaler
scal=MinMaxScaler()
#Load the saved model
model=pkl.load(open("Rfc_model.p","rb"))
# model.fit(X_train,y_train)

st.set_page_config(page_title="Brain Stroke Predictor App",page_icon="⚕️",layout="centered",initial_sidebar_state="expanded")

def preprocess(gender,age,hypertension,heart_disease,ever_married,residence_type,avg_glucose_level,bmi ):
    
    if gender == "Male" or gender == "male" or gender == "M":
        gender = 0
    else:
        gender = 1
        
    if hypertension == "Yes":
        hypertension = 1
    else:
        hypertension = 0
    
    if heart_disease == "Yes":
        heart_disease = 1
    else:
        heart_disease = 0
        
    if ever_married == "Yes":
        ever_married = 1
    else:
        ever_married = 0
        
    if Residence_type == "urban":
        Residence_type = 1
    else:
        Residence_type = 0
    
        
    pred = model.predict([[gender,age,hypertension,heart_disease,ever_married,Residence_type,avg_glucose_level,bmi ]])
    return pred[0]




age = st.selectbox ("Age",range(1,82,1))
gender = st.radio("Select Gender: ", ('Male', 'Female'))
hypertension = st.radio("Hypertension", ['Yes','No']) 
heart_disease = st.radio("Ever had heart issues", ['Yes','No'])
ever_married = st.radio("Married?", ['Yes','No'])
avg_glucose_level = st.selectbox('Glucose Level',range(1,300,1))
bmi = st.selectbox('Glucose Level',range(1,300,1))
residence_type = st.radio("Residence Type",['Urban','Rural'])
# g = input("Enter your gender : ")
# g = g.lower()

# a = int(input("Enter your age : "))

# hyt = input("Do you have hypertension ? yes or no : ")
# hyt = hyt.lower()

# ht = input("Do you have any heart Disease ? yes or no : ")
# ht = ht.lower()

# m = input("Have you been Married ? yes or no : ")
# m = m.lower()


# r = input("residency type ? rural or urban ? : ")
# r = r.lower()

# gl = input('enter glucose levels. ? Enter value or type "i do not know" : ' )
# gl = gl.lower()

# b = int(input("Enter BMI"))


pred = preprocess(gender,age,hypertension,heart_disease,ever_married,Residence_type,avg_glucose_level,bmi)

if pred == 0:
    st.error('Warning! You have high risk of getting a stroke!')

else:
    st.success('You have lower risk of getting a stroke!')

st.sidebar.subheader("About App")

st.sidebar.info("This web app is helps you to find out whether you are at a risk of developing a brain stroke.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check are you at risk or not!!")
st.sidebar.info("Don't forget to rate this app")



feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)


if feedback:
    st.header("Thank you for rating the app!")
    st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.") 
        
    

    
    
   






import streamlit as st
import pickle
import sklearn
import numpy as np


def load_model():
    with open('saved_model.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

rfc = data["model"]
# sc = data["sc"]

def show_predict_page():

    st.set_page_config(page_title="Brain Stroke Predictor App",page_icon="⚕️",layout="centered",initial_sidebar_state="expanded")


    st.title(" Stroke Prediction ")

    st.write("### Please provide the necessary details")

show_predict_page()


def preprocess(gender,age,hypertension,heart_disease,ever_married,residence_type,Work_Type,avg_glucose_level,bmi ):

    # if gender == "Male":
    #     gender = 0
    # else:
    #     gender = 1
    #
    # if hypertension == "Yes":
    #     hypertension = 1
    # else:
    #     hypertension = 0
    #
    # if heart_disease == "Yes":
    #     heart_disease = 1
    # else:
    #     heart_disease = 0
    #
    # if ever_married == "Yes":
    #     ever_married = 1
    # else:
    #     ever_married = 0
    #
    # if residence_type == "Urban":
    #     residence_type = 1
    # else:
    #     residence_type = 0
    #
    # if Work_Type == "Government Job":
    #     Work_Type = 0
    # elif Work_Type == "Never Worked":
    #     Work_Type = 1
    # elif Work_Type == "Private":
    #     Work_Type = 2
    # elif Work_Type == "Self Employed":
    #     Work_Type = 3
    # else:
    #     Work_Type = 4
    user_input=[gender,age,hypertension,heart_disease,ever_married,residence_type,Work_Type,avg_glucose_level,bmi ]
    user_input=np.array(user_input)
    user_input=user_input.reshape(1,-1)
    prediction = rfc.predict(user_input)
    # print(gender,age,hypertension,heart_disease,ever_married,residence_type,Work_Type,avg_glucose_level,bmi )
    # pred = rfc.predict([[gender,age,hypertension,heart_disease,ever_married,residence_type,avg_glucose_level,bmi,Work_Type ]])
    # print(pred)
    return prediction

Gender = st.selectbox("Select your gender :", range(0,2,1))

Age = st.selectbox("What is your age ?",range(1,82,1))

hypertension = st.selectbox("Do you have hypertension?", range(0,2,1))

heart_disease = st.selectbox("Do you have or had any heart related issues", range(0,2,1))

Marriage_status = st.selectbox("What is your marital status ?" ,  range(0,2,1))

Residence_Type = st.selectbox("What is your residence type - Urban or Rural", range(0,2,1))

Glucose_level = st.slider("Enter your average glucose level ?",50.0,280.0)

BMI = st.slider("Enter your Body Mass Index value ?" , 10.0,95.0)

Work_type = st.selectbox("What is your work type ? ", range(0,5,1))

preds = preprocess(Gender,Age,hypertension,heart_disease,Marriage_status,Residence_Type,Glucose_level,BMI,Work_type)
print(Gender,Age,hypertension,heart_disease,Marriage_status,Residence_Type,Glucose_level,BMI,Work_type)
print(preds)

if st.button("Predict"):
    if preds == 0:
        st.success("You have a lower risk of getting stroke !")

    elif preds == 1:
        st.error("Warning! You have high risk of getting a stroke")



st.sidebar.subheader("About App")

st.sidebar.info("This web app is helps you to find out whether you are at a risk of developing a brain stroke.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check are you at risk or not!!")
st.sidebar.info("Don't forget to rate this app")



feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)


if feedback:
    st.header("Thank you for rating the app!")
    st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.")


print(sklearn.__version__)
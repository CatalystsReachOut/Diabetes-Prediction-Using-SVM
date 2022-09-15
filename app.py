import imp


import pickle
from soupsieve import select
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model
diabetes_model = pickle.load(open("diabetesmodel.sav","rb"))

# sidebar for navigate

with st.sidebar:
    selected=option_menu('Sugar Prediction System',[
        "Diabetes Prediction"
    ],

    # bootstrap icons
    icons=["activity"],
    default_index=0
    )


# Diabetes Prediction Page
if(selected=="Diabetes Prediction"):

    # page title
    st.title("Diabetes Prediction Using SVM")

    # getting the input data from the user
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number Of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI Level")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.text_input("Age Of Patient")

    # prediction
    diabetes_diagnosis=""

    # creating button for prediction
    if st.button("Diabetes Test Result"):
        diabetes_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        # diabetes_prediction=diabetes_model.predict([[-0.84488505, -1.12339636 ,-0.16054575  ,0.53090156, -0.69289057 ,-0.68442195 ,-0.36506078, -0.19067191]])
        print(diabetes_prediction)
        if(diabetes_prediction[0]==1):
            diabetes_diagnosis="This person is Diabetic"
        else:
            diabetes_diagnosis="This person is Non-Diabetic"
    st.success(diabetes_diagnosis) 
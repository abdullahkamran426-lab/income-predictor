import streamlit as st
import requests

st.title("income predictor")
st.write("Enter the details below to predict if the income is >50K or <=50K")

age = st.number_input("Age", min_value=0, max_value=100, value=30)

# Merged broken lines 9 and 10
workclass = st.selectbox("Workclass", ["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"])                         

# Merged and cleaned up broken lines 12 and 13
education = st.selectbox("Education", ["Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"])

marital_status = st.selectbox("Marital Status", ["Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"])
occupation = st.selectbox("Occupation", ["Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct ", "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv", "Armed-Forces"])
relationship = st.selectbox("Relationship", ["Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"])   
gender = st.selectbox("Gender", ["Female", "Male"])
capital_gain = st.number_input("Capital Gain", min_value=0, value=0)
capital_loss = st.number_input("Capital Loss", min_value=0, value=0)
hours_per_week = st.number_input("Hours per week", min_value=0, max_value=168, value=40)
native_country = st.selectbox("Native Country", ["United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany", "Outlying-US(Guam-USVI-etc)", "India", "Japan", "Greece", "South", "China", "Cuba", "Iran", "Honduras", "Philippines", "Italy", "Poland", "Jamaica", "Vietnam", "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic", "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala", "Nicaragua", "Scotland", "Thailand", "Yugoslavia", "El-Salvador", "Trinadad&Tobago", "Peru", "Hong", "Holand-Netherlands"]) 
if st.button("Predict"):
    data = {
        "age": age,
        "workclass": workclass,
        "education": education,
        "marital_status": marital_status,           
        "occupation": occupation,
        "relationship": relationship,
        "gender": gender,
        "capital_gain": capital_gain,
        "capital_loss": capital_loss,
        "hours_per_week": hours_per_week,
        "native_country": native_country
    }   
    
    try:
        # Changed 'localhost' to '127.0.0.1' to avoid Windows connection bugs
        response = requests.post("https://abdullahkamran426-income-predictor-backend.hf.space/predict", json=data, timeout=5)
        
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"Predicted Income: {prediction}")
        else:
            # This will show you exactly WHAT the backend didn't like (e.g., 422, 404, 500)
            st.error(f"Backend Server replied with Status Code: {response.status_code}")
            try:
                st.json(response.json())  # Shows validation rules you broke
            except:
                st.text(response.text)    # Shows raw errors
                
    except requests.exceptions.ConnectionError:
        st.error("Connection Failed! Your backend server is NOT running on port 8000, or it crashed.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")


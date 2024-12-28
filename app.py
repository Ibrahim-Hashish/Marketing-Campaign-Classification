import streamlit as st
import pickle

# Load the saved Random Forest model
with open("random_forest_model.pkl", 'rb') as file:
    model = pickle.load(file)

# Define a function to predict the Response
def predict_response(features):
    prediction = model.predict([features])
    return "Yes, The Customer will response to marketing campign" if prediction[0] == 1 else "No, The Customer willnot response to the marketing campign"

st.title("Marketing Response Prediction")
st.write("""This app predicts whether a customer will respond to a marketing campaign based on their behavioral data.""")

# User Input
st.header("Enter Customer Details")

# Collect inputs for all features
Age = st.number_input("Age", min_value=18, max_value=100, value=30)
Education = st.selectbox("Education Level", options=["Basic", "Graduation", "PhD", "Master", "2n Cycle"])
Income = st.number_input("Income", min_value=0, value=20000)
Kidhome = st.number_input("Number of Kids at Home",min_value=0, max_value=10, value=0)
Teenhome = st.number_input("Number of Teenagers at Home", min_value=0, max_value=10, value=0)
Dt_Customer = st.date_input("Date of Customer Enrollment")
Recency = st.number_input("Recency (Days)", min_value=0, value=10)
MntWines = st.number_input("Amount Spent on Wines", min_value=0, value=0)
MntFruits = st.number_input("Amount Spent on Fruits", min_value=0, value=0)
MntMeatProducts = st.number_input(
    "Amount Spent on Meat Products", min_value=0, value=0)
MntFishProducts = st.number_input(
    "Amount Spent on Fish Products", min_value=0, value=0)
MntSweetProducts = st.number_input(
    "Amount Spent on Sweets", min_value=0, value=0)
MntGoldProds = st.number_input(
    "Amount Spent on Gold Products", min_value=0, value=0)
NumDealsPurchases = st.number_input(
    "Number of Deals Purchases", min_value=0, value=0)
NumWebPurchases = st.number_input(
    "Number of Web Purchases", min_value=0, value=0)
NumCatalogPurchases = st.number_input(
    "Number of Catalog Purchases", min_value=0, value=0)
NumStorePurchases = st.number_input(
    "Number of Store Purchases", min_value=0, value=0)
NumWebVisitsMonth = st.number_input(
    "Number of Web Visits per Month", min_value=0, value=0)
AcceptedCmp3 = st.selectbox("Accepted Campaign 3?", options=["No", "Yes"])
AcceptedCmp4 = st.selectbox("Accepted Campaign 4?", options=["No", "Yes"])
AcceptedCmp5 = st.selectbox("Accepted Campaign 5?", options=["No", "Yes"])
AcceptedCmp1 = st.selectbox("Accepted Campaign 1?", options=["No", "Yes"])
AcceptedCmp2 = st.selectbox("Accepted Campaign 2?", options=["No", "Yes"])
Complain = st.selectbox("Has Customer Complained?", options=["No", "Yes"])
Marital_Status = st.selectbox("Marital Status", options=[
                              "Divorced", "Married", "Single", "Together", "Widow"])
Z_CostContact = st.number_input("Z Cost Contact", min_value=0, value=0)
Z_Revenue = st.number_input("Z Revenue", min_value=0, value=0)

# Encode categorical variables
AcceptedCmp3 = 1 if AcceptedCmp3 == "Yes" else 0
AcceptedCmp4 = 1 if AcceptedCmp4 == "Yes" else 0
AcceptedCmp5 = 1 if AcceptedCmp5 == "Yes" else 0
AcceptedCmp1 = 1 if AcceptedCmp1 == "Yes" else 0
AcceptedCmp2 = 1 if AcceptedCmp2 == "Yes" else 0
Complain = 1 if Complain == "Yes" else 0

# One-hot encoding for Marital Status
Marital_Status_Divorced = 1 if Marital_Status == "Divorced" else 0
Marital_Status_Married = 1 if Marital_Status == "Married" else 0
Marital_Status_Single = 1 if Marital_Status == "Single" else 0
Marital_Status_Together = 1 if Marital_Status == "Together" else 0
Marital_Status_Widow = 1 if Marital_Status == "Widow" else 0

# One-hot encoding for Education
Education = 0 if Education == "Basic" else 1 if Education == "Graduation" else 2 if Education == "Master" else 3 if Education == "PhD" else 4

features = [
    Age, Education, Income, Kidhome, Teenhome, Dt_Customer.toordinal(
    ), Recency, MntWines, MntFruits,
    MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds,
    NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases,
    NumWebVisitsMonth, AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, AcceptedCmp1,
    AcceptedCmp2, Complain, Z_CostContact, Z_Revenue, Marital_Status_Divorced, Marital_Status_Married,
    Marital_Status_Single, Marital_Status_Together, Marital_Status_Widow
]

# Prediction Button
if st.button("Predict"):
    result = predict_response(features)
    st.subheader(f"The model predicts: {result}")

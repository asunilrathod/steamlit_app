import streamlit as st
import pandas as pd
import joblib

# Load your pre-trained model
model = joblib.load('D:\practice\your_model.pkl')  # Replace with the path to your model file

# Streamlit app title
st.title('Fraud Detection App')

# Create input fields for user to input data
st.write("Enter transaction details:")
step = st.number_input('Step', min_value=0)
amount = st.number_input('Amount', min_value=0.01, value=0.01)
oldbalanceOrg = st.number_input('Old Balance Org', min_value=0.01, value=0.01)
newbalanceOrig = st.number_input('New Balance Orig', min_value=0.01, value=0.01)
oldbalanceDest = st.number_input('Old Balance Dest', min_value=0.01, value=0.01)
newbalanceDest = st.number_input('New Balance Dest', min_value=0.01, value=0.01)
type_CASH_OUT = st.checkbox('Is Cash Out?')
type_DEBIT = st.checkbox('Is Debit?')
type_PAYMENT = st.checkbox('Is Payment?')
type_TRANSFER = st.checkbox('Is Transfer?')

# Create a button to make predictions
if st.button('Predict Fraud'):
    # Create a pandas DataFrame with user input
    user_input = pd.DataFrame({
        'step': [step],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest],
        'type_CASH_OUT': [1 if type_CASH_OUT else 0],
        'type_DEBIT': [1 if type_DEBIT else 0],
        'type_PAYMENT': [1 if type_PAYMENT else 0],
        'type_TRANSFER': [1 if type_TRANSFER else 0]
    })
    
    # Make predictions using your model
    prediction = rf.predict(user_input)
    
    # Display the prediction result
    if prediction[0] == 1:
        st.error('Fraudulent Transaction')
    else:
        st.success('Not Fraudulent Transaction')
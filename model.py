import streamlit as st
import pandas as pd
import pickle
import ast
import numpy as np
import sklearn

def run():
    # Load Dependencies
    with open('model_scaler.pkl', 'rb') as file_1:
        model_scaler = pickle.load(file_1)

    with open('knn_model.pkl', 'rb') as file_2:
        knn_model = pickle.load(file_2)

    # Initialize y_pred_inf as None
    y_pred_inf = None

    # Create Streamlit input widgets for user input
    limit_balance = st.number_input(label='Please enter your limit balance', min_value=0, max_value=999999999999, value=0)
    pay_1 = st.number_input(label='Please enter your pay 1', min_value=-12, max_value=12, value=0, key=12)
    pay_2 = st.number_input(label='Please enter your pay 2', min_value=-12, max_value=12, value=0, key=11)
    pay_3 = st.number_input(label='Please enter your pay 3', min_value=-12, max_value=12, value=0, key=10)
    pay_4 = st.number_input(label='Please enter your pay 4', min_value=-12, max_value=12, value=0, key=15)
    pay_5 = st.number_input(label='Please enter your pay 5', min_value=-12, max_value=12, value=0, key=17)
    pay_6 = st.number_input(label='Please enter your pay 6', min_value=-12, max_value=12, value=0, key=20)

    # Create a dataframe to hold the user input data
    data_inf = pd.DataFrame({
        'limit_balance': [limit_balance],
        'pay_1': [pay_1],
        'pay_2': [pay_2],
        'pay_3': [pay_3],
        'pay_4': [pay_4],
        'pay_5': [pay_5],
        'pay_6': [pay_6]
    })

    # Display the user input data in a table
    st.table(data_inf)

    # When the "Prediksi" button is clicked
    if st.button(label='Prediksi'):
        # Separate numerical and categorical features
        data_inf_num = data_inf[['limit_balance']]
        data_inf_cat = data_inf[['pay_1', 'pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6']]

        # Preprocess numerical features
        data_inf_num_scaled = model_scaler.transform(data_inf_num)

        # Concatenate numerical and categorical features
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat], axis=1)

        # Predict using the pre-trained model
        y_pred_inf = knn_model.predict(data_inf_final)

    # Show result
    if y_pred_inf is not None:
        if y_pred_inf[0] == 0:
            prediction = "Nasabah diprediksi gagal melakukan pembayaran"
        else:
            prediction = "Nasabah diprediksi dapat melunasi pembayaran"
            
        st.write(f"{prediction}")

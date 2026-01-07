import streamlit as st
import helper
import joblib

model = joblib.load("models/best_model.pkl")

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('These questions are likely duplicates')
    else:
        st.header('These questions are not duplicates')
        
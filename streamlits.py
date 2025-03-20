import streamlit as st

st.title("Simple Streamlit App")

user_input = st.text_input("Enter your name")

if st.button("Submit"):
    st.write(f"Hello, {user_input}!")
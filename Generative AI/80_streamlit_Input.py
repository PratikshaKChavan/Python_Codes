import streamlit as st

st.title("Programming by Pratiksha Kalyan Chavan")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome {name}")

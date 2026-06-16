import streamlit as st

st.title("Programming by Pratiksha Kalyan Chavan")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success("PDF Uploaded Successfully")

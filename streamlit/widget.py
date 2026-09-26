import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name")

age=st.slider("Enter your age:",0,100,25)

options=["Python","Java","C++","JavaScript"]
choice=st.selectbox("Select an option",options)
st.write(f"You selected {choice}")

st.write("your age is:",age)
if name:
    st.write(f"Hello, {name}")

data = {
    "name":["John","Jake","Jane","Jill"],
    "age":[18,21,23,25],
    "city":["New York","Los Angeles","Chicago","Houston"],
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Upload your file")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
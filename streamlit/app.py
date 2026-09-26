import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlit")

## simple text
st.write("This is simple text")

## Create a simple data frame
df=pd.DataFrame({
    'first column':[1,2,3],
    'second column':[10,20,30]
})

## display the data frame
st.write("Here is a dataframe")
st.write(df)

## Create a line chart
chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)




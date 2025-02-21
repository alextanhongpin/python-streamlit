import streamlit as st

number = st.number_input("Insert a number")
st.write("The current number is ", number)

integer = st.number_input("Insert an int", step=1, min_value=1, max_value=10)
st.write("The current int is ", integer)

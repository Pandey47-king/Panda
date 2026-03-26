import streamlit as st
import pandas as pd

st.title("Books")
st.header("भक्तो को मेरा नमस्कार")
st.subheader("The Bhagavad Gita, Ramayana, and Ramcharitmanas teach us dharma, duty, morality, and the true art of living")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

#with st.container():
#    st.subheader("BhagavadGita")
#    st.image("artifacts/images/BhagavadGita.jpg")
#    st.subheader("Ramayan")
#    st.image("artifacts/images/Ramayan.jpg")
#    st.subheader("Ramcharitmanas")
#    st.image("artifacts/images/Ramcharitmanas.jpg")
#    st.subheader("On the way of krishna")
#    st.image("artifacts/images/On the way of krishna.jpg")

col1, col2, col3, col4 = st.columns([2, 2, 2, 2],gap="medium",vertical_alignment='center',border=True)
col1.write("BhagavadGita")
col1.image("artifacts/images/BhagavadGita.jpg")
col1.write("**₹639**")
col2.write("Ramayan")
col2.image("artifacts/images/Ramayan.jpg")
col2.write("**₹802**")
col3.write("Ramcharitmanas")
col3.image("artifacts/images/Ramcharitmanas.jpg")  
col3.write("**₹1,495**")
col4.write("On the way of krishna")
col4.image("artifacts/images/On the way of krishna.jpg") 
col4.write("**₹399**")
st.radio("Select one:", ["BhagavadGita", "Ramayan","Ramcharitmanas","On the way of krishna"])

st.text_input("Enter Your name")
st.text_input("Enter your Contact no")
st.text_input("Enter your Email Id")
st.text_area("Enter your full address",placeholder="Mumbai")
if st.button("Submit"):
    st.switch_page('pages/form_feedback.py')

 
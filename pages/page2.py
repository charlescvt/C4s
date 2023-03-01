import streamlit as st
import requests
from streamlit_lottie import st_lottie
from st_html import formsubmit
from st_functions import *
from st_summ import main

st.title("Call 4 Short")

ticker = st.text_input("Ticker")
if ticker:
    st.write(ticker+"! I love it...")
quarter = st.text_input("Quarter")
if quarter:
    st.write("Ah yess. " + quarter + "... What a great time to have been alive")

gs = st.button("Get Summary")
if gs:
    st.write("Boom! Let's gooo \n")
    summary = main(ticker, quarter)
    st.subheader("Summary: \n")
    st.text(summary)

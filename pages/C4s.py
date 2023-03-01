import streamlit as st
import requests
from streamlit_lottie import st_lottie
from st_html import formsubmit
from st_functions import *
from st_summ import main

st.title("Call 4 Short")

# input ticker
ticker = st.text_input("Ticker")
if ticker:
    st.write(ticker+"! How original...")

# input quarter
quarter = st.text_input("Quarter (~Format: QX 20XX)")
if quarter:
    st.write(quarter + "... Weren't you so much happier back then?")

gs = st.button("Get Summary")
if gs:
    st.markdown("Engines running! Sit back and relax while I do all the work <br> This should take a couple of minutes.")
    st.write("Oh and by the way, this is the company right? Ok good. Come back in a bit!")
    image_url = dalle_image(ticker +' logo')
    st.image(image_url, caption=ticker)
    while st.spinner():
        summary = main(ticker, quarter)
        st.subheader("Summary: \n")
        st.text(summary)
        st.stop()

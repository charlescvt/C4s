import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page

import requests
import smtplib
from email.message import EmailMessage
import openai
import os

from st_html import formsubmit

openai.api_key = os.environ.get("OPENAI_API_KEY")

st.set_page_config(page_title="Retained Earnings",
        page_icon=':bar_chart:',
        layout='wide')

def get_lottie(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

lottie_finance = get_lottie("https://assets5.lottiefiles.com/packages/lf20_qfkv85bq.json")

with st.container():
    one, two, three = st.columns(3)
    with one:
        st.subheader("Hey there! Welcome to")
        st.title("Retained Earnings")
        st.header("Interactive info for developed palates.")
        st.write("Click the button below to start or scroll down to learn more about the product.")
    with three:
        st_lottie(lottie_finance, width=300)

with st.container():
    st.write('---')
    st.markdown("<h1 style='text-align: center; color: white;'>Our programs so far</h1>", unsafe_allow_html=True)
    st.write('---')
    st.write('&nbsp;')

    one, two, three = st.columns(3)
    with one:
        st.header("Call 4 Short")
        c4sbutton = st.button("Try C4S")
        if c4sbutton:
            switch_page('page2')
        st.subheader("1. Collects earnings transcript from API")
        st.subheader("2. Passes transcript through ChatGPT to create augmented terminal")
        st.subheader("3. Interactive chatbot Q&A")

    with two:
        st.header("Dash, the cool Dashboard")
        mtadbutton = st.button("Try Dash")
        if mtadbutton:
            switch_page('page2')
        st.subheader("1. Selects up to three companies")
        st.subheader("2. Diverse financial analyses on stock and options prices")
        st.subheader("3. Understand data through real-time visualization")



st.write('&nbsp;')
st.write('---')

with st.form("Contact Form"):

    st.subheader("Contact Info")
    st.text("Name: Charles Chaverot")
    st.text("Email: charleschav01@ucla.edu")
    st.write('&nbsp;')

    st.subheader("Give me your feedback or a funny joke")

    left, right = st.columns(2)
    with left:
        name = st.text_input("Name")
    with right:
        email = st.text_input("E-mail")
    message = st.text_input("Message")

    submitted = st.form_submit_button("Submit")


st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:charleschav01@ucla.edu?subject=Call4Short&body=Please specify the issue you are facing with the app.'><strong>Charles Chaverot</strong></a></center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)

    # if submitted:
    #     # send me an email with the message
    #     msg = EmailMessage()
    #     msg.set_content('Name: ' + name +
    #                     '\nE-mail: ' + email +
    #                     '\nMessage: ' + message)

    #     msg['Subject'] = 'New message from RE user'
    #     msg['From'] = name
    #     msg['to'] = 'cchaverot@gmail.com'

    #     s = smtplib.SMTP('server.smtp.com')
    #     s.send_message(msg)
    #     s.quit()

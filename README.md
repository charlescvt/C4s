---
# C4s | Company reports and augmented AI terminal
---

## Introduction

Call 4 Short (or C4s, for short) is a tool that financial analysts can use to quickly access company reports and interpret the data with the help of ChatGPT. The project aims to implement the usage of various APIs, multiple-file programming and stock data analysis, all wrapped in a Streamlit-based efficient web app. 
<br> 
<br>
So far, C4s is built on the following components:
1. Seeking Alpha's REST Client API to query for earnings calls of the user's choosing (Company and Quarter).
2. OpenAI API to feed the retrieved data to GPT 3.5, making it learn the current company status from pages of transcript.
3. An augmented ChatGPT terminal where the user can interact with the AI to ask for insights on the company's operations.
4. COMING SOON: Tome AI implementation for quick slides generation to visualize earnings-call transcript.


## Instructions for use:
1. Install necessary Python libraries <br>
In order to run C4s, you will need some Python libraries installed on your computer such as OpenAI's ChatGPT API, Streamlit and other minor ones. The process takes **less than a minute** and the requirements are **packaged into the "requirements.txt" file** in the repo so you can run a `pip install -r requirements.txt` and have everything you need!

2. Save OpenAI API key on your environment as OPENAI_API_KEY <br>
Find your key at https://platform.openai.com/account/api-keys and follow the steps below to save it on your environment:
- MacOS: https://youngstone89.medium.com/setting-up-environment-variables-in-mac-os-28e5941c771c
- Windows: https://phoenixnap.com/kb/set-environment-variable-mac
- To keep it short (house rules), you will run some form of `export OPENAI_API_KEY = <your_API_key>` in your terminal. 

3. From your terminal run `streamlit run Home.py` and the website's (hopefully) clear instructions will take it from there.


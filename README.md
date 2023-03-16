---
# C4s | Quick access to company reports with insightful AI-based interpretation
---

## Introduction

Call 4 Short (or C4s, for short) is a tool that financial analysts can use to quickly access company reports and interpret the data with the help of ChatGPT. The project aims to implement the usage of various APIs, multiple-file programming and stock data analysis, all wrapped in a Streamlit-based efficient web app. 
<br> 
<br>
So far, C4s is built on the following components:
1. A REST Client API which queries Seeking Alpha for earnings calls of the user's choosing (Company and Quarter)
2. The ChatGPT API which feeds the retrieved data to the AI, allowing it to understand the current company status from pages of transcript.
3. An augmented ChatGPT terminal where the user can interact with the AI to ask for insights on the company's operations.
4. COMING SOON: Tome AI implementation for quick slides visualization of the earnings-call transcript.


## Instructions for use:
In order to run OpenAi's ChatGPT and Dall-E, you will need to save your API Key in your program environment under the name 'OPENAI_API_KEY'.

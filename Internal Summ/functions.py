import requests
from bs4 import BeautifulSoup
from datetime import datetime

# to access the internet
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

# to access official ChatGPT API once it comes out
#mport openai

# to load login data from revChatGPT package
from revChatGPT.V1 import Chatbot
import importlib.resources
import json

def user_input():
        """
        Input: user input of company ticker, quarter and year of transcript desired

        Output: this is a mechanical function that simply transforms user input for efficient
        use with the Seeking Alpha API later

        """
        start = time.time()
        # Ask for company ticker and quarter of transcript desired
        ticker = input("Ok, what's the ticker of the company?\n").lower()
        info_quarter = input("""What quarter are we looking at? \n
        (For example, for the third quarter of 2021, type "Q3 2021") \n""")

        # setting interval to collect all transcript data from
        quarter = info_quarter.split()[0]

        # past year because of weird timings like WMT (e.g Q4 2023 in January)
        past_year = int(info_quarter.split()[1]) - 1
        next_year = past_year+1

        since_ts = datetime.strptime(('01/01/' + str(past_year)),
                                                    '%m/%d/%Y').strftime("%s")
        until_ts = datetime.strptime(('01/01/' + str(next_year)),
                                                    '%m/%d/%Y').strftime("%s")

        end = time.time()
        print ("Received user input in " + str(round(end-start,2)) + " seconds")
        return ticker, quarter, since_ts, until_ts


def sa_api(ticker, quarter, since_ts, until_ts):
    """
    Input: information about company ticker, quarter (i.e Q3) and
    beginning/end of the year desired

    Output: dictionary w/ transcript data and link of the transcript for
    that company at that quarter of that year
    """

    start = time.time()

    # API url
    url = "https://seeking-alpha.p.rapidapi.com/transcripts/v2/list"


    querystring = {"id": ticker,"size":"10","number":"1",
                'since': since_ts, 'until': until_ts}

    headers = {
        "X-RapidAPI-Key": "8827e09261msh7aa755f62cee90ap1fc6d4jsneb412fed1336",
        "X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
    }


    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)

    for i in range (len(result['data'])):
        transcript = result['data'][i]

        if quarter in transcript['attributes']['title']:
            final_transcript_data = transcript
            transcript_link = ('https://seekingalpha.com' + transcript['links']['self'])

    if final_transcript_data == None:
        return "We couldn't find your transcript"

    end = time.time()
    print ("Retrieved transcript info in " + str(round(end-start, 2)) + " seconds")

    return final_transcript_data, transcript_link


def get_tr_text(link):

    start = time.time()

    wd = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    response = requests.get(link)

    soup = BeautifulSoup(response.content, "html.parser")

    text = soup.get_text()

    # cut useless intro before Company Participants and add "Company Participants" back :)
    result = 'Company Participants ' + text.split('Company Participants')[1]

    end = time.time()
    print ("Retrieved transcript text in " + str(round(end-start,2)) + " seconds")

    return result

def text_splitter(text):

    chunks = []
    j=2500
    while len(text)!=0:
        segment = ' '.join(text.split()[0:2500])
        #print(segment+'\n')
        chunks.append(segment)


        text = ' '.join(text.split()[2500:])

    return chunks

def ask_chatgpt(prompt=None):
    # loading config file

    start = time.time()

    with importlib.resources.open_text("revChatGPT", "config.json") as file:
        config_file = json.load(file)
    if prompt == None:
        prompt = input("Prompt: ")

    # initiating chatbot
    chatbot = Chatbot(config=config_file)

    *_, response = chatbot.ask(prompt, conversation_id='fcdb1ecb-121b-47da-93b4-db51cbae8973')

    end = time.time()
    print ("ChatGPT terminal initiated in " + str(round(end-start,2)) + " seconds")


    return response["message"]

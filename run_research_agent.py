import os
from colorama import Fore
import requests
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from bs4 import BeautifulSoup 
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import json
# from autogen import config_list_from_json
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
from autogen import UserProxyAgent
import autogen

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# from langchain_community.callbacks import get_openai_callback
# from langchain_openai import OpenAI

print(f"{Fore.YELLOW}---------------------Loading Environment Varaibles---------------------{Fore.RESET}")

load_dotenv()
os.environ['AUTOGEN_USE_DOCKER'] = '0'
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # OpenAI API Key saved in local var for global use
SERP_API_KEY = os.getenv("SERP_API_KEY") # OpenAI API Key saved in local var for global use
GPT_MODEL = os.getenv("GPT_MODEL")
CONFIG_LIST =  [ # OpenAI API Key and model saved in config list for simplicity with agents
            {
                "model": GPT_MODEL,
                "api_key": OPENAI_API_KEY,
            }
        ]
# config_list = config_list_from_json("OAI_CONFIG_LIST")

#function to check previously searched urls
"""
Note to Self: Add previously searched URLS to the DB;
- Exception: Not news sites that will have new articles but the same URL
"""

# Function to perform a Google search using the Serper API
def google_search(search_keyword):    
    url = "https://google.serper.dev/search"

    payload = json.dumps({
        "q": search_keyword
    })

    headers = {
        'X-API-KEY': SERP_API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(f"{Fore.GREEN}---------------------Search Complete---------------------{Fore.RESET}")
    print("RESPONSE:", response.text)
    return response.text

# Summarizes the given content based on the specified objective using a specified LLM
def summary(objective, content):
    llm = ChatOpenAI(temperature = 0, model = GPT_MODEL)

    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size = 10000, chunk_overlap=500)
    docs = text_splitter.create_documents([content])
    
    map_prompt = """
    Write a summary of the following text for {objective}:
    "{text}"
    SUMMARY:
    """
    map_prompt_template = PromptTemplate(template=map_prompt, input_variables=["text", "objective"])
    
    summary_chain = load_summarize_chain(
        llm=llm, 
        chain_type='map_reduce',
        map_prompt = map_prompt_template,
        combine_prompt = map_prompt_template,
        verbose = False
    )

    output = summary_chain.run(input_documents=docs, objective=objective)

    return output

# Scrapes the given URL and extracts relevant data from the web page.
def web_scraping(objective: str, url: str):
    #Note: will summarize the content based on objective if the content is too large
    #objective is the original objective & task that user give to the agent, url is the url of the website to be scraped

    print(f"{Fore.YELLOW}---------------------Scraping website---------------------{Fore.RESET}")

    response = selinium_scrape(url)
    print(f"{Fore.YELLOW}---------------------Scrape Response---------------------{Fore.RESET}")

    if response != "":
        soup = BeautifulSoup(response, "html.parser")
        text = soup.get_text()
        text = clean_soup_text(text)

        if len(text) > 10000:
            output = summary(objective, text)
            return output
        else:
            return text
    else:
        print(f"{Fore.RED}HTTP request failed with status code {response}{Fore.RESET}")  
        return f"HTTP request failed with status code {response}"

# Uses Selenium to scrape the given URL and extract relevant data from the web page.
def selinium_scrape(url):

    # Using WebDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get(url)

    # Check the current URL
    current_url = driver.current_url
    print(f"{Fore.GREEN}Current URL:", current_url, f"{Fore.RESET}")

    page_content = driver.page_source

    driver.quit()

    return page_content

# Cleans and extracts text from a BeautifulSoup object by removing unwanted tags and whitespace.
def clean_soup_text(text):
    # Remove all the newlines
    text = text.replace("\n", " ")
    # Remove all the extra spaces
    text = " ".join(text.split())
    return text

# Creates and initializes research agents for conducting automated research tasks.

def create_user_proxy():
    # Create user proxy agent
    print(f"{Fore.YELLOW}---------------------Create user proxy agent---------------------{Fore.RESET}")
    user_proxy = UserProxyAgent(name="user_proxy",
        is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
        max_consecutive_auto_reply=1,
        )
    
    return user_proxy

def create_research_agent():
    # Create researcher agent
    print(f"{Fore.YELLOW}---------------------Create researcher agent---------------------{Fore.RESET}")
    researcher = GPTAssistantAgent(
        name = "researcher",
        description = "Researcher agent",
        llm_config = {
            "config_list": CONFIG_LIST,
            "assistant_id": "asst_Nt9WR0jReC1JgQ88fYJEjwAg"
        }
    )

    print(f"{Fore.YELLOW}---------------------Register researcher functions---------------------{Fore.RESET}")
    researcher.register_function(
        function_map={
            "web_scraping": web_scraping,
            "google_search": google_search,
            "check_url": check_url
        }
    )

    return researcher

def create_research_manager_agent():
    # Create research manager agent
    print(f"{Fore.YELLOW}---------------------Create research manager agent---------------------{Fore.RESET}")
    research_manager = GPTAssistantAgent(
        name="research_manager",
        description="Research manager agent",
        llm_config = {
            "config_list": CONFIG_LIST,
            "assistant_id": "asst_Qn0WmtmBn6gl9eJRursaWfrX"
        }
    )
    return research_manager

def run_groupchat(user_proxy, researcher, research_manager, message):
    # Create group chat

    print(f"{Fore.YELLOW}---------------------Create Groupchat---------------------{Fore.RESET}")

    groupchat = autogen.GroupChat(agents=[user_proxy, researcher, research_manager], messages=[], max_round=15)

    group_chat_manager = autogen.GroupChatManager(groupchat=groupchat, llm_config={"config_list": CONFIG_LIST})


    # Start the chat
    print(f"{Fore.YELLOW}---------------------Initalize Groupchat---------------------{Fore.RESET}")

    response = user_proxy.initiate_chat(group_chat_manager, clear_history=True, message=message, silent=False)

    print(f"{Fore.GREEN}---------------------Search Complete---------------------{Fore.RESET}")
    # print(response)

    response_researcher = return_reseacher_responses(response.chat_history)

    return response_researcher

def return_reseacher_responses(chat_history):
    # Extract all messages from the researcher in order
    researcher_messages = [message['content'] for message in chat_history if message.get('name') == 'researcher']
    return researcher_messages


message = "What is wrong with the Intel i13 and newer chips?"
researcu_results = run_groupchat(create_user_proxy(), create_research_agent(), create_research_manager_agent(), message)

print(f"{Fore.GREEN}---------------------Research Results:---------------------{Fore.RESET}")
print(researcu_results)

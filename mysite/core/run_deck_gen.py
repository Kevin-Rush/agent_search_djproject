import os

import markdown
from colorama import Fore
from dotenv import load_dotenv
import json

# import script_converter
# import slide_deck_generator
# import slide_image_gen

from .run_research_agent import run_search
from core import openai_gen

"""
Information flow:

n fields to build the user prompt:
- Document type
- Audience
- Purpose
- Additional information
- File name

Display the user prompt to the user for validation
- If the user is satisfied with the prompt, proceed to subsections
- If not, ask for the user to edit prompt directly


"""

# Input file
# file_name = "biz_dev_test"

# input_file = "scripts/"+file_name+".txt"
# json_script = "scripts/"+file_name+".json"
# base_ppxt = 'base_presentation.pptx'

# For testing only

load_dotenv("../.env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # OpenAI API Key saved in local var for global use

"""
Ask for all config information required:
- OpenAI API Key
- Model Type (Note can give cost expectations per model)
- Serper (or FireCrawl ... TBD) API Key

n fields to build the user prompt:
- Document type (business development, business analysis, marketing, etc.)
-- Note the actual document will be ppxt by default, other file types will be added in the future
- Audience
- Purpose
- Additional information
- File name

Display the user prompt to the user for validation
- If the user is satisfied with the prompt, proceed to sections
- If not, ask for the user to edit prompt directly
"""

api_key = OPENAI_API_KEY

print(f"{Fore.YELLOW}ATTENTION:{Fore.RESET}")
print(f"""You are about to generate a slide deck based on the information you provide to the following questions. \n\n
      In a single phrase, what type of document are you creating? \n
      Who is the audience for this document? \n
      What are you trying to achieve with this document? \n
      Any additional information about the document or the subject matter would like to include? \n
      What would you like to name the file? \n
      """)

doc_type = input("In a single phrase, what type of document are you creating? ")
audience = input("Who is the audience for this document? ")
purpose = input("What are you trying to achieve with this document? ")
additional_info = input("Any additional information about the document or the subject matter would like to include? ")
file_name = input("What would you like to name the file? ")

system_prompt = "You are a expert AI assistant that is here to help create a " + doc_type + " document for " + audience + " with the purpose of " + purpose + ". " + " Here is additional conext for this document: " + additional_info + ". You will be asked to do multiple tasks to complete this document. Always remember to respond in JSON format so that I can handle your responses simply. Please do the best you can because the user is counting on you!"

outline_prompt = "Can you please write a detailed outline for the requested document?" 

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": outline_prompt},
]

results = openai_gen.run_text_gen(messages, api_key=api_key)
results = openai_gen.get_response_json(results)

print(json.dumps(results, indent=4))

# results_markdown = run_search(user_prompt)
# results_html = markdown.markdown(results_markdown)

# print(results_markdown)
import os

import markdown
# import script_converter
# import slide_deck_generator
# import slide_image_gen
from dotenv import load_dotenv

from .run_research_agent import run_search

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

key = OPENAI_API_KEY
model = os.getenv("GPT_MODEL")
doc_type = input("What type of document are you creating? ")
audience = input("Who is the audience for this document? ")
purpose = input("What is the purpose of this document? ")
additional_info = input("Any additional information you would like to include? ")
file_name = input("What would you like to name the file? ")

user_prompt = "Create a " + doc_type + " document for " + audience + " with the purpose of " + purpose + ". " + " Here is additional conext for this document: " + additional_info + ". " 

results_markdown = run_search(user_prompt)
# results_html = markdown.markdown(results_markdown)

print(results_markdown)
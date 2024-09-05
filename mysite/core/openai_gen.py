import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv("../.env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # OpenAI API Key saved in local var for global use
GPT_MODEL = os.getenv("GPT_MODEL")

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def run_chat_completion(messages, model=GPT_MODEL):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        response_format={"type": "json_object"}
    )

    return chat_completion

def get_prompt_usage(chat_completion):
    return chat_completion.usage.prompt_tokens

def get_completion_usage(chat_completion):
    return chat_completion.usage.completion_tokens

def get_total_usage(chat_completion):
    return chat_completion.usage.total_tokens

def get_response(chat_completion):
    return chat_completion.choices[0].message.content
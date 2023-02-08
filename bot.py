from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
completion = openai.Completion()

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nChatbot:"
restart_sequence = "\nYou:"
session_prompt = "You are talking with Santiago, a GPT3 bot influencer that was mentored by Elon Musk"

'''
  Code copied from Website for developers.
  Prompt text
'''
def ask(question, chat_log=None):
  prompt_text = f'{chat_log}{restart_sequence}:{question}{start_sequence}'
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt_text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=['\n']
  )
  story = response['choices'][0]['text']
  return str(story)

'''
  This function will help the bot to remember
'''
def append_interaction_to_chat_log(question, answer, chat_log=None):
  if chat_log is None:
    chat_log = session_prompt
  return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
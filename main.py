import openai
import streamlit as st
from openai import OpenAI
from generateImage import generateImage
from input import takeInput


model_choice, prompt, api_key, imagequality_choice,imagesize_choice, imageamount_choice = takeInput()
# Configure the client
client = OpenAI(api_key=api_key)

# generate image and display it
try:
     generateImage(client=client, model_choice=model_choice, prompt=prompt,imagequality_choice=imagequality_choice, imagesize_choice=imagesize_choice, imageamount_choice=imageamount_choice)
except openai.APIError as e:
    #Handle API error here, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")

except openai.APIConnectionError as e:
    #Handle connection error here
    print(f"Failed to connect to OpenAI API: {e}")

except openai.RateLimitError as e:
    #Handle rate limit error (we recommend using exponential backoff)
    print(f"OpenAI API request exceeded rate limit: {e}")

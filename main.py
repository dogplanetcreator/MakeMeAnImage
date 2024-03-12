import openai
import streamlit as st
from openai import OpenAI
from generateImage import generateImage
from input import takeInput

CURRENT_THEME = "dark"

model_choice, prompt, api_key, imagequality_choice,imagesize_choice, imageamount_choice = takeInput()
# Configure the client
client = OpenAI(api_key=api_key)

# generate image and display it

generateImage(client=client, model_choice=model_choice, prompt=prompt,imagequality_choice=imagequality_choice, imagesize_choice=imagesize_choice, imageamount_choice=imageamount_choice)

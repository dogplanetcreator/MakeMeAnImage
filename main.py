import openai
import streamlit as st
from openai import OpenAI
from generateImage import generateImage
from input import takeInput


prompt, api_key, imagequality_choice, imagesize_choice, imageamount_choice= takeInput()
# Configure the client
client = OpenAI(api_key=api_key)



# generate image and display it

generateImage(api_key=api_key,client=client, prompt=prompt,imagequality_choice=imagequality_choice, imagesize_choice=imagesize_choice, imageamount_choice=imageamount_choice)

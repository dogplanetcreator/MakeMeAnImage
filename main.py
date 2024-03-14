import openai
import streamlit as st
from openai import OpenAI
from generateImage import generateImage
from input import takeInput


model_choice, prompt, api_key, imagequality_choice, imagesize_choice, imageamount_choice, saveimage_choice, imagesavepath, imagesaveprefix = takeInput()
# Configure the client


if api_key=="":
            # Display message about missing api key
            st.write('API Key missing')
else:
 client = OpenAI(api_key=api_key)

# generate image and display it

generateImage(client=client, model_choice=model_choice, prompt=prompt,imagequality_choice=imagequality_choice, imagesize_choice=imagesize_choice, imageamount_choice=imageamount_choice,saveimage_choice=saveimage_choice,imagesavepath=imagesavepath,imagesaveprefix=imagesaveprefix)

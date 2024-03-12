import openai
import streamlit as st
import requests
import time
from io import BytesIO
from PIL import Image
from openai import OpenAI


def generateImage(client, model_choice, prompt,imagequality_choice,imagesize_choice, imageamount_choice):
      
    if st.button("Generate Image"):
              
        # Logic if prompt is empty
        if prompt== "":
            # Display message about missing prompt
            st.write('Prompt missing')
        else:
             # adding 20 seconds time delay
            time.sleep(70)
            
            for n in range(1, imageamount_choice+1):

                # create the image generation request
                response = client.images.generate(
                    model=model_choice,
                    prompt=prompt,
                    size=imagesize_choice,
                    quality=imagequality_choice,
                    n=imageamount_choice
                    )
           
                
                image_url = response.data[0].url
                print("Generated Image URL:", image_url)

                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))

                # Display the image
                st.image(img)
                
                # adding 20 seconds time delay
                time.sleep(70)

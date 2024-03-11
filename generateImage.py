import openai
import streamlit as st
import requests
from io import BytesIO
from PIL import Image
from openai import OpenAI


def generateImage(client, model_choice, prompt,imagequality_choice):
      
    if st.button("Generate Image"):
              
        # Logic if prompt is empty
        if prompt== "":
            # Display message about missing prompt
            st.write('Prompt missing')
        else:
            try:
                # create the image generation request
                response = client.images.generate(
                    model=model_choice,
                    prompt=prompt,
                    size="1024x1024",
                    quality=imagequality_choice,
                    n=1
                    )
            except openai.APIError as e:
                #Handle API error here, e.g. retry or log
                print(f"OpenAI API returned an API Error: {e}")
                pass
            except openai.APIConnectionError as e:
                #Handle connection error here
                print(f"Failed to connect to OpenAI API: {e}")
                pass
            except openai.RateLimitError as e:
                #Handle rate limit error (we recommend using exponential backoff)
                print(f"OpenAI API request exceeded rate limit: {e}")
                pass
            else:
                
                image_url = response.data[0].url
                print("Generated Image URL:", image_url)

                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))

                # Display the image
                st.image(img)
                


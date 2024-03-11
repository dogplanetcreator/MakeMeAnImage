import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import openai


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
                image_url = response.data[0].url
                print("Generated Image URL:", image_url)

                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))

                # Display the image
                st.image(img)
            
            except openai.error.Timeout as e:
                #Handle timeout error, e.g. retry or log
                print(f"OpenAI API request timed out: {e}")
                pass
            except openai.error.APIError as e:
                #Handle API error, e.g. retry or log
                print(f"OpenAI API returned an API Error: {e}")
                pass
            except openai.error.APIConnectionError as e:
                #Handle connection error, e.g. check network or log
                print(f"OpenAI API request failed to connect: {e}")
                pass
            except openai.error.InvalidRequestError as e:
                #Handle invalid request error, e.g. validate parameters or log
                print(f"OpenAI API request was invalid: {e}")
                pass
            except openai.error.AuthenticationError as e:
                #Handle authentication error, e.g. check credentials or log
                print(f"OpenAI API request was not authorized: {e}")
                pass
            except openai.error.PermissionError as e:
                #Handle permission error, e.g. check scope or log
                print(f"OpenAI API request was not permitted: {e}")
                pass
            except openai.error.RateLimitError as e:
                #Handle rate limit error, e.g. wait or log
                print(f"OpenAI API request exceeded rate limit: {e}")
                pass
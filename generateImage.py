import openai
import streamlit as st
import requests
import time
import urllib 
from urllib import request
import urllib.request
import shutil
from io import BytesIO
from PIL import Image
from openai import OpenAI



def generateImage(client, model_choice, prompt,imagequality_choice,imagesize_choice, imageamount_choice,saveimage_choice,imagesavepath,imagesaveprefix):
      
    if st.button("Generate Image"):
              
        # Logic if prompt is empty
        if prompt== "":
            # Display message about missing prompt
            st.write('Prompt missing')
            
        else:
         if saveimage_choice=="Yes" and imagesavepath=="":
                 st.write('Path for saving image missing')

         else:    


            for a in range(1, imageamount_choice+1):

                 try:
                     # create the image generation request
                     response = client.images.generate(
                     model=model_choice,
                     prompt=prompt,
                     size=imagesize_choice,
                     quality=imagequality_choice,
                     n=1
                 )
                 except openai.RateLimitError as e:
                  #Handle rate limit error (we recommend using exponential backoff)
                     #delay next try
                     time.sleep(80)
                     try:
                         # create the image generation request
                         response = client.images.generate(
                         model=model_choice,
                         prompt=prompt,
                         size=imagesize_choice,
                         quality=imagequality_choice,
                         n=1
                     )
                   
                     except openai.RateLimitError as e:
                      #Handle rate limit error (we recommend using exponential backoff)      
                      print(f"OpenAI API request exceeded rate limit: {e}")
                      pass
                     except openai.APIError as e:
                      #Handle API error here, e.g. retry or log
                      print(f"OpenAI API returned an API Error: {e}")
                      pass
                     except openai.APIConnectionError as e:
                        #Handle connection error here
                        print(f"Failed to connect to OpenAI API: {e}")
                        pass
                     except openai.ServiceUnavailableError as e:
                      # Handle 5xx errors here
                      print(f"OpenAI API request error: {e}")
                      pass
                 pass

                
                 image_url = response.data[0].url
                 print("Generated Image URL:", image_url)

                
                 response = requests.get(image_url)
                 img = Image.open(BytesIO(response.content))

                 if saveimage_choice=="Yes":
                    #Save the image
                    imagesavepathandname=str(str(imagesavepath) + str(imagesaveprefix) + str(a) + ".jpg")
                    with open(imagesavepathandname, "wb") as f:
                     f.write(response.content)
                     f.save
                     f.close
                   
                    # Display the image
                    st.image(img) 
                    st.write(imagesavepathandname)
                 
                 else:
                    # Display the image
                    st.image(img)

                 

                    
                 
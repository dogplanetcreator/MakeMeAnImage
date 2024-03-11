import streamlit as st
import requests
from io import BytesIO
from PIL import Image

def generateImage(client, model_choice, prompt,imagequality_choice):
    if st.button("Generate Image"):
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
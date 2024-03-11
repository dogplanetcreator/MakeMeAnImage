from openai import OpenAI
from generateImage import generateImage
from input import takeInput


model_choice, prompt, api_key, imagequality_choice = takeInput()
# Configure the client
client = OpenAI(api_key=api_key)
# generate image and display it
try:
    generateImage(client=client, model_choice=model_choice, prompt=prompt,imagequality_choice=imagequality_choice)

except openai.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except openai.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except openai.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
import openai
from openai import OpenAI
from generateImage import generateImage
from input import takeInput


model_choice, prompt, api_key, imagequality_choice = takeInput()
# Configure the client
client = OpenAI(api_key=api_key)
# generate image and display it
try:
    generateImage(client=client, model_choice=model_choice, prompt=prompt,imagequality_choice=imagequality_choice)

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
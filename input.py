import streamlit as st


def takeInput():
    # Title
    st.title('Make me an Image')
    # Ask for the API key
    api_key = st.text_input("Enter your OpenAI API key:", type="password")
    # Ask for the model choice
    model_choice = st.selectbox(
        "Which Dall E model would you like to use? ",
        ("DALL·E 3", "DALL·E 2"),
        index=None,
        placeholder="Select DALL·E model",
    )
    # Display user choice
    st.write('You selected:', model_choice)
    
 # Ask for the image quality
    imagequality_choice = st.selectbox(
        "Which image quality would you like to use? ",
        ("standard", "hd"),
        index=None,
        placeholder="Select image quality",
    )
    # Display user choice
    st.write('You selected:', imagequality_choice)

    # Logic if no model is selected
    if model_choice == "DALL·E 3":
        model_choice = "dall-e-3"
    else:
        model_choice = "dall-e-2"

    # Logic if quality is selected
    if imagequality_choice == "hd":
        imagequality_choice = "hd"
        model_choice = "dall-e-3"
        # Display change user choice
        st.write('When selecting quality', imagequality_choice)
        st.write('Dall E model is set to:', model_choice)
        
    else:
        imagequality_choice = "standard"
        st.write('Dall E model is set to:', model_choice)
        st.write('Image quality is set to', imagequality_choice)

    # Takes the user prompt
    prompt = st.text_input("Enter a prompt:")

    

    return model_choice, prompt, api_key, imagequality_choice
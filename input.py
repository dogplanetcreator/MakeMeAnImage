import streamlit as st


def takeInput():
    # Title
    st.title('Dog Planet Image AI')
    # Ask for the API key
    api_key = st.text_input("Enter your OpenAI API key:", type="password")

    # Ask for the model choice
    model_choice = st.selectbox(
        "You can only use DALL E 3, DALL E 2 are no longer available ",
        ("DALL·E 3",""),
        index=0,
        
    )
    # Display user choice
    model_choice = "dall-e-3"

    st.write('You are using:', model_choice)
    
 
 
    


         # Ask for the quality of images Dall E 3
    imagequality_choice = st.selectbox(
            "Quality of images?",
            ("standard","hd"),
            index=0,
           
        )

        # Ask for the size of images Dall E 3
    imagesize_choice = st.selectbox(
            "Size of images?",
            ("1024x1024","1792x1024","1024x1792"),
            index=0,
          
        )
        
         # Ask for the number of images
    imageamount_choice = st.selectbox(
            "How many images would you like to create? ",
            (1,2,3,4,5,6,7,8,9,10),
            index=0,
          
        )

         

     # Takes the user prompt
    prompt = st.text_input("Enter a prompt:")

    
    return model_choice, prompt, api_key, imagequality_choice,imagesize_choice, imageamount_choice
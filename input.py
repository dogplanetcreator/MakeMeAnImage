import streamlit as st


def takeInput():
    # Title
    st.title('Dog Planet Image AI')
    # Ask for the API key
    api_key = st.text_input("Enter your OpenAI API key:", type="password")

    # Ask for the model choice
    model_choice = st.selectbox(
        "Which Dall E model would you like to use? ",
        ("DALL·E 3", "DALL·E 2"),
        index=1,
        
    )
    # Display user choice
    st.write('You selected:', model_choice)
    
 
 
    # Logic if model is selected
    if model_choice == "DALL·E 3":
        model_choice = "dall-e-3"

         # Ask for the quality of images Dall E 3
        imagequality_choice = st.selectbox(
            "Quality of images?",
            ("standard","hd"),
            index=1,
           
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
            ("1"),
            index=0,
          
        )    

        # Display user choice
        st.write('You selected image quality:', imagequality_choice)
        st.write('You selected image size:', imagesize_choice)
        st.write('You can only create image amount:', imageamount_choice)

    else:
        model_choice = "dall-e-2"

        
        # Image quality can be only standard
        imagequality_choice="standard"
        st.write('You can only use quality:', imagequality_choice)

        # Ask for the size of images Dall E 2
        imagesize_choice = st.selectbox(
            "Size of images?",
            ("256x256", "512x512","1024x1024"),
            index=2,
          
        )
        # Display user choice
        st.write('You selected:', imagesize_choice)

        # Ask for the number of images
        imageamount_choice = st.selectbox(
            "How many images would you like to create? ",
            ("1", "2","3","4","5","6","7","8","9","10"),
            index=0,
            
        )
        # Display user choice
        st.write('You selected:', model_choice)
        st.write('You selected image quality:', imagequality_choice)
        st.write('You selected image size:', imagesize_choice)
        st.write('You selected image amount:', imageamount_choice)


    # Takes the user prompt
    prompt = st.text_input("Enter a prompt:")

    

    return model_choice, prompt, api_key, imagequality_choice,imagesize_choice, imageamount_choice
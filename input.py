import streamlit as st


def takeInput():
    # Title
    st.title('Dog Planet Image AI')
    # Ask for the API key
    api_key = st.text_input("Enter your OpenAI API key:", type="password")

    model_choice="dall-e-3"

  

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

         # Ask if images shall be saved locally
        #saveimage_choice = st.selectbox(
            #"Save images on your disk?",
            #("Yes","No"),
            #index=1,
        #saveimage_choice = "No"
        #)

          # Logic if save is selected
       # if saveimage_choice == "Yes":
            # Takes the file path to existing work path and file name prefix
            #st.write('Images are saved to', Path.cwd)
            #imagesaveprefix = st.text_input("Enter a filename prefix:") 
            #
            #imagesavepath = st.text_input("Enter a path for saving images:")

        #else:
        #imagesavepath =""
        #imagesaveprefix =""
   


        # Display user choice
        #st.write('You selected image quality:', imagequality_choice)
        #st.write('You selected image size:', imagesize_choice)
        #st.write('You selected image amount:', imageamount_choice)

   
            

    st.write('You selected image quality:', imagequality_choice)
    st.write('You selected image size:', imagesize_choice)
    st.write('You selected image amount:', imageamount_choice)


    # Ask if images shall be saved locally
        #saveimage_choice = st.selectbox(
           # "Save images on your disk?",
           # ("Yes","No"),
           # index=1,
       # saveimage_choice = "No"   
        #)
         
          # Logic if save is selected
       # if saveimage_choice == "Yes":
           # Takes the file path to existing work path and file name prefix
            #st.write('Images are saved to', Path.cwd)
            #imagesaveprefix = st.text_input("Enter a filename prefix:") 
            #
            #imagesavepath = st.text_input("Enter a path for saving images:")

            
        #else:
        #imagesavepath =""
        #imagesaveprefix =""
   

     # Takes the user prompt
    prompt = st.text_input("Enter a prompt:")

    
    return model_choice, prompt, api_key, imagequality_choice,imagesize_choice, imageamount_choice
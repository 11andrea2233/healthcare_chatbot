import streamlit as st
from streamlit_option_menu import option_menu
import openai

#Sidebar menu options
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
openai.api_key = api_key

with st.sidebar:
    page = option_menu(
        "Dashboard",
        ["Home", "About Me", "Healthcare AI Chatbot"],
        icons=['house', '🩺',  'file-text'],
        menu_icon="list",
        default_index=0,
    )
    
if not api_key:
    st.warning("Please enter your OpenAI Key to proceed.")
    
else:
    if page == "Home" :
         st.title ("AI-Powered Receptionist Chatbot for Healthcare")
         
    
    elif page == "About Me":
        st.header("About Me")
        
    elif page == "Healthcare AI Chatbot":
        System_prompt = """
        """
        
        def initialize_conversation(prompt):
            if 'message' not in st.session_state:
                st.session_state.message = []
                st.session_state.message.append({"role": "system", "content": System_prompt})
                
            initialize_conversation(System_prompt)
            
            for messages in st.session_state.message:
                if messages['role'] == 'system':
                    continue
                else:
                    with st.chat_message(messages["role"]):
                        st.markdown(messages["content"])

            if user_message := st.chat_input("I can only answer questions related to healthcare"):
                with st.chat_message("user"):
                    st.markdown(user_message)
                st.session_state.message.append({"role": "user", "content": user_message})
                chat = openai.ChatCompletion.create(
                    model="gpt-4o-mini",
                    messages=st.session_state.message,
                )
                response = chat.choices[0].message.content
                with st.chat_message("assistant"):
                    st.markdown(response)
                st.session_state.message.append({"role": "assistant", "content": response})
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
         st.write("Hello there! I am your new AI receptionist, designed to make life easier for both healthcare providers and patients. Think of me as a virtual assistant that can help answer patient questions, schedule appointments, provide medication reminders, handle basic billing inquiries, and share information about the clinic. I am here to make sure patients get the answer they need quickly and securely, while freeing up staff to focus on more important tasks.")
         st.write("What makes me special? Well, I use advanced technology to look up the right information and respond accurately, like an efficient, friendly receptionist. I am always available and ready to assist, whether its early in the morning or late at night.")
        
         st.write("What can I do?")
         st.write("1. Scheduling Appointments. You can book, reschedule or cancel appointments without having to wait on hold or visit the clinic in person.")
         st.write("2. Medication Reminders. I can remind patients of their current medications and help them request refills, saving everyone time.")
         st.write("3. Billing Questions. For simple billing questions, I can look up amounts and payment dates, and if things get too complicated, it will direct you to the billing team.")
         st.write("4. General Clinic Information. Whether its clinic hours, location or accepted insurance plans, i have all the details to keep patients informed.")
        
         st.write("Purpose")
         st.write("My job is simple: to take on the routine questions so your healthcare team can focus on what matters most—caring for patients! Here is how I help:")
         st.write("Save Time: By handling common questions, I give staff more time to focus on patient care.")
         st.write("Answer Quickly: Patients dont have to wait long for answers about appointments, medications, and billing—I can respond almost instantly!")
         st.write("Protect Privacy: I make sure all patient information is kept safe and secure, following healthcare privacy rules.")
         
    
    elif page == "About Me":
        st.header("About Me")
        st.markdown("""
        Hi! I'm Andrea Sombilon! I am a business intelligence specialist and data analyst with a strong foundation in deriving insights from data to drive strategic decisions. Currently, I am expanding my skill set by learning to create products in Artificial Intelligence and working towards becoming an AI Engineer. My goal is to leverage my expertise in BI and data analysis with advanced AI techniques to create innovative solutions that enhance business intelligence and decision-making capabilities. 
        
        This projects is one of the projects I am building to try and apply the learning I have acquired from the AI First Bootcamp of AI Republic.
        
        Any feedback would be greatly appreciated! ❤           
                    """)
        
        
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

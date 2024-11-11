import os
import streamlit as st
from streamlit_option_menu import option_menu
import openai
import base64

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

        Role:
            You are an AI receptionist working for a healthcare provider. Your goal is to assist patients with administrative tasks such as appointment scheduling, medication reminders, general clinic information, and basic billing inquiries. You are the first point of contact for patients, providing friendly, professional, and efficient service while maintaining strict patient confidentiality.
            Your tone should be warm and welcoming, yet professional, to ensure that patients feel comfortable and valued in every interaction. You should be mindful of each patient's unique needs and treat each inquiry with care and respect.
            
        Instructions:
            Verify Patient Identity:
                Verification Process: Start every interaction involving patient-specific information by requesting the patient’s ID or their full name and date of birth. This ensures secure access to personal health information.
                Contextual Verification: Use verification only when accessing sensitive information; if the question is general (e.g., clinic hours), provide an immediate response without verification.
            Provide Administrative Assistance:
                Appointment Scheduling and Management: Check provider availability and assist with booking, rescheduling, or canceling appointments. Ensure that each interaction is clearly documented for accurate scheduling.
                Follow-up Appointments: For patients with recent visits, proactively ask if they need a follow-up based on their recent diagnosis or treatment.
                Medication Reminders and Refills: Offer reminders for current medications and refills, if requested. If the patient asks for a medication change or clinical question, politely redirect them to a healthcare provider.
                Billing Inquiries: Answer basic billing questions, such as amounts and billing dates, once the patient’s identity is verified. If questions are complex or detailed, suggest that the patient contact the billing department.
                General Clinic Information: Provide details such as clinic hours, accepted insurance providers, clinic location, and contact numbers.
            Escalate Medical and Complex Inquiries:
                Medical Advice: If the patient asks a clinical question or seeks medical advice (e.g., questions about symptoms, treatment options, or medical diagnoses), respond politely by redirecting them to the healthcare provider or an appropriate department.
                Specialized Department Contact: For inquiries that require a specific department (e.g., billing issues, insurance questions, or detailed medical records), offer to connect the patient to the relevant team.
            Offer Additional Help and Conclude with Care:
                After completing a task, always ask if there is anything else you can assist with. Use phrases like "Is there anything else I can help you with today?" or "Please feel free to ask if you have any more questions."
            
        Context:
            You have secure, role-based access to a patient dataset and clinic information, including:
            Basic Patient Details: Patient ID, name, DOB, contact information, emergency contact, and address.
            Health Details: Current conditions, allergies, current medications, and most recent visit.
            Appointment History: Past appointment dates and scheduled future appointments.
            Insurance Information: General information about the insurance provider (not specific policy details).
            Clinic Operational Details: Working hours, address, accepted insurance plans, provider names and specializations, contact numbers, and other non-personal information.
            Sensitive information such as diagnoses, medical test results, or provider notes are restricted to authorized personnel only, and you should never access or disclose these details without proper patient authorization.
            
        Constraints:
            Privacy and Data Security:
                Always adhere to HIPAA compliance and healthcare privacy regulations. Ensure that all interactions involving personal health information (PHI) are securely verified.
                Only access and display information relevant to the patient’s specific query to minimize the exposure of sensitive information.
            Limitations on Data Disclosure:
                Do not disclose detailed information about diagnoses, test results, or treatment plans.
                Limit access to billing details unless the patient has been verified.
                Do not answer questions about other family members without their direct authorization.
            Scope of Assistance:
                Focus on administrative tasks. Politely decline and redirect any clinical or medical advice requests.
                Maintain professionalism even if the patient becomes frustrated or requests services outside your capabilities.
            Escalation Protocol:
                For any questions or tasks that fall outside the scope of administrative tasks or require a human touch (e.g., patient complaints, sensitive billing issues, or urgent medical inquiries), follow escalation protocols by connecting the patient to the appropriate department.
            
        Examples:
            Example 1: Appointment Scheduling
            Patient: "I need to book a follow-up appointment with Dr. Smith."
            AI Receptionist: "Of course, I can help you with that. Could you please provide your Patient ID or your full name and date of birth for verification?"
            (Once verified)
            "Thank you, [Patient’s Name]. I see Dr. Smith has availability on Thursday at 3 PM. Would that work for you?"
            
            Example 2: Medication Inquiry
            Patient: "Can you remind me what medication I’m on?"
            AI Receptionist: "Certainly! To ensure privacy, may I have your Patient ID or your full name and date of birth?"
            (Once verified)
            "Thank you. According to our records, your current medication is [Medication Name and Dosage]. Please let us know if you’d like to request a refill or speak with your provider about this medication."
    
            Example 3: Billing Inquiry
            Patient: "I have a question about a charge on my last bill."
            AI Receptionist: "I’d be happy to help. May I have your Patient ID or your name and date of birth to verify your account?"
            (Once verified)
            "Thank you. Your last charge was for [Service] on [Date]. For a detailed breakdown or questions about insurance, I recommend speaking with our billing department. Would you like me to connect you with them?"
            
            Example 4: General Clinic Information
            Patient: "What time does the clinic open on Saturdays?"
            AI Receptionist: "Our clinic opens at 9 AM on Saturdays and closes at 3 PM. Is there anything else I can help you with?"
        
        """

        st.markdown("""
        <style>
        .user-message {
            background-color: rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
            margin-left: auto;
            margin-right: 0;
            max-width: 80%;
            text-align: right;
        }
        .assistant-message {
            background-color: rgba(255, 255, 255, 0.1) !important;
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
            margin-right: auto;
            margin-left: 0;
            max-width: 80%;
            text-align: left;
        }
        .stChatMessage > div {
            background-color: transparent !important;
        }
        .stChatMessage [data-testid="UserAvatar"] {
            float: right;
        }
        </style>
    """, unsafe_allow_html=True)
        
        #Initialize chat history
        if 'messages' not in st.session_state:
            st.session_state.messages = []
            
        #display chat messages from history on app return
        for message in st.session_state.messages:
            message_class = "user-message" if message ["role"] == "user" else "assistant-message"
            with st.chat_message(message["role"], avatar = "👨" if message["role"] == "user" else "👩‍⚕️"):
                   st.markdown(f'<div class="{message_class}">{message["content"]}</div>', unsafe_allow_html=True)
        
        # Accept user input
        if prompt := st.chat_input("How can I assist you?"):
            # Exit command handling
            if prompt.lower() in ['exit', 'quit']:
                with st.chat_message("assistant", avatar="👨"):
                    st.markdown('<div class="assistant-message">I hope I was able to assist you today!.</div>', unsafe_allow_html=True)
                st.stop()
        
        # Display user message in chat message container
        with st.chat_message("user", avatar="👨"):
            st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate chatbot response
        messages = [{'role': 'system', 'content': System_prompt}] + st.session_state.messages
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages
        ).choices[0].message.content

        # Display assistant response in chat message container
        with st.chat_message("assistant", avatar="👩‍⚕️"):
            st.markdown(f'<div class="assistant-message">{response}</div>', unsafe_allow_html=True)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

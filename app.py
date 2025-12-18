import streamlit as st


st.title("Ai Chatbot")

# messages = [
#     {
#         "role": "Ai",
#         "content": "Hello! How can i help you today?"
#     },
#     {
#         "role": "User",
#         "content": "Can you tell me a joke?"
#     },
#     {
#         "role": "Ai",
#         "content": "Sure! why did the scarecrow win an award? because he was outstandin in his  field"
#     }
# ]
from google import genai
from dotenv import load_dotenv
import os
client = genai.Client(api_key="AIzaSyC_Mr95SLQ61qdbAizCCnWIfzkhdmbtYi4")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
        "role" : "ai",
        "content": "Hello! How can i help you today?"
    }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input =st.chat_input("Enter your message here...")
if user_input:
    st.session_state.messages.append(
        {
        "role": "User",
        "content" : user_input

    })
    with st.chat_message("User"):
        st.markdown(user_input)
     ##short term memory
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= list(map(lambda message: message["role"]+ 
        message["content"], st.session_state.messages ))
    )

    st.session_state.messages.append(
        {
        "role" : "ai",
        "content" : response.text
    })

    with st.chat_message("ai"):
        st.markdown(response.text)


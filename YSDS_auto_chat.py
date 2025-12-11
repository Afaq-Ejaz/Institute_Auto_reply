import os
from groq import Groq 
from dotenv import load_dotenv
import streamlit as st
import time

load_dotenv()

client= Groq(
    api_key=os.getenv("Grok_api"))

st.title("📗🖋 Yashfeen Virtual Assistant")

st.badge("Your Quick Admission Assistant", color="blue")

user_input = st.text_input("What's Your Query: ")

button = st.button("GO !")

print(button)

if button:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature= 0.5,
        messages=[
            {

                "role": "system",
                "content": """You are a virtual assisatant of an institute names Yashfeen Skill Development Services , 
                You will be keep updating the user prompts and you will be answering the user queries related to the admission process and other queries related to the institute.
                If the user asks for any other question you just generate the response that it is not a related question.
                if the user greets you then ask him about admission, tell user that these are high tech courses and free of cost.
                Yashfeen Skill Development Services is offering a various courses that includes, you will show courses in a list format:

                1. Python Programming
                2. Web Development
                3. Graphic Designing
                4. Digital Marketing
                
                You will ask about the name and eduction, these courses are available for university students (Bachelors and upwards) excpet
                graphic designing which is available for matriculation students.
                and at last when the user specifies its course,name and other data, ask him to contact Miss Kainat who is the incharge of 
                these courses, her contact number is 0321-4244227.
                                
                """
                
                
            },
            {
                "role": "user",
                "content": user_input,
            }
        ],

    )

    think = st.progress(2 , text="Thinking...")
    time.sleep(2)
    think.empty()
    st.write(response.choices[0].message.content)


        # api_key=os.environ.get("GROQ_API_KEY"),

    # print(response.choices[0].message.content)



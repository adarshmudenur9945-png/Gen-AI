#loading the environmental file
from dotenv import load_dotenv
load_dotenv()

#Create Chat groq object and invoke it
from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-120b")

while(True):
    query = input("Ask Anything...")
    if query.lower() in ["exit", "quit"]:
        print("Good Bye...")
        break
    res=llm.invoke(query)
    print(res.content)

import streamlit as st
st.title("My Buddy - Langchain and Groq based AI assistant")
st.markdown("It assists me in my learning of GenAI")
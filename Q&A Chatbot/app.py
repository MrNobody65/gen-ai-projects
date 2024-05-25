# Q&A Chatbot
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv() # take environment variables from .env

import streamlit as st
import os

## Function to load OpenAI model and get responses

def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name="davinci-002", temperature=0.5)
    response = llm(question)
    return response

## Initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input ", key="input")

submit = st.button("Ask the question")
response = get_openai_response(input)

## If ask button is clicked

if submit:
    st.subheader("The response is")
    st.write(response)
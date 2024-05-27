import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from LLama 2 model

def getLLama2response(input_text, no_words, blog_style):


    ### LLama 2 model
    llm = CTransformers(model="llama-2-7b-chat.ggmlv3.q8_0.bin", model_type='llama', config={'max_new_tokens': 256, 'temperature': 0.01})

    ### Prompt template
    template = """Write a blog for {style} job profile for a topic {text} within {n_words} words."""

    prompt = PromptTemplate(input_variables=["style", "text", "n_words"], template=template)

    response = llm(prompt.format(style=blog_style, text=input_text, n_words=no_words))
    return response

st.set_page_config(page_title="Generate Blogs", layout="centered", initial_sidebar_state="collapsed")

st.header("Generate Blogs")

input_text = st.text_input("Enter the Blog Topic")

## Create two more columns for additional two fields


col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input("No of Words")

with col2:
    blog_style = st.selectbox("Writing the blog for", ('Researchers','Data Scientist','Common People'), index=0)

submit = st.button("Generate")

## Final response
if submit:
    st.write(getLLama2response(input_text, no_words, blog_style))
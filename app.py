import streamlit as st
import openai
import os
from text_summarizer.functions import summarize
from text_summarizer.functions import findkeypoints
from text_summarizer.functions import generatequestions

openai.api_key = os.getenv('OPENAI_KEY')

if "summary" not in st.session_state:
    st.session_state["summary"] = ""

if "pr" not in st.session_state:
    st.session_state["pr"] = ""
if "keypoints" not in st.session_state:
    st.session_state["keypoints"] = ""
if "questions" not in st.session_state:
    st.session_state["questions"] = ""   


    
    
st.title("Medical Text Summarizer")

input_text = st.text_area(label="Enter full text:", value="", height=250)

st.button(
    "Medical Summary",
    on_click=summarize,
    kwargs={"prompt": input_text},
)
st.button(
    "Key points",
    on_click=findkeypoints,
    kwargs={"prompt": input_text},
)
st.button(
    "question generation",
    on_click=generatequestions,
    kwargs={"prompt": input_text},
)

Prompt_field = st.text_area(label="Prompt:", value=st.session_state["pr"], height=100)
summary = st.text_area(label="Summary:", value=st.session_state["summary"], height=200)
keypoints = st.text_area(label="Key Points:", value=st.session_state["keypoints"], height=200)
questions = st.text_area(label="questions:", value = st.session_state["questions"], height=200)

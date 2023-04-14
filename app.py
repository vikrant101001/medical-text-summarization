import streamlit as st
import openai
import os
from text_summarizer.functions import summarize
from text_summarizer.functions import findkeypoints
from text_summarizer.functions import generatequestions

st.set_page_config(layout="wide")

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

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.button(
        "Medical Summary",
        on_click=summarize,
        kwargs={"prompt": input_text},
    )
 
with col2:
    st.button(
        "Key points",
        on_click=findkeypoints,
        kwargs={"prompt": input_text},
    )
    
with col3:
    st.button(
        "question generation",
        on_click=generatequestions,
        kwargs={"prompt": input_text},
    )

   
Prompt_field = st.text_area(label="Prompt:", value=st.session_state["pr"], height=100)

res1, res2, res3 = st.columns(3)

with res1:
    summary = st.text_area(label="Summary:", value=st.session_state["summary"], height=200)
with res2:
    keypoints = st.text_area(label="Key Points:", value=st.session_state["keypoints"], height=200)
with res3:
    questions = st.text_area(label="questions:", value = st.session_state["questions"], height=200)

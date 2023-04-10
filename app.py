import streamlit as st
import openai
import os
from text_summarizer.functions import summarize
from text_summarizer.functions import questiongenerate

openai.api_key = os.getenv('OPENAI_KEY')

if "summary" not in st.session_state:
    st.session_state["summary"] = ""

st.title("Medical Text Summarizer")

input_text = st.text_area(label="Enter full text:", value="", height=250)

st.button(
    "Submit for GPT 3-summarization",
    on_click=summarize,
    kwargs={"prompt": input_text},
)
st.button(
    "Submit for BioGPT-summarization",
    on_click=summarize,
    kwargs={"prompt": input_text},
)
st.button(
    "Submit for GPT 3-question generation",
    on_click=questiongenerate,
    kwargs={"prompt": input_text},
)


output_text = st.text_area(label="Results:", value=st.session_state["summary"], height=250)

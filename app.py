import streamlit as st
import openai
import os
from text_summarizer.functions import summarize


openai.api_key = os.getenv('OPENAI_KEY')

if "summary" not in st.session_state:
    st.session_state["summary"] = ""

if "pr" not in st.session_state:
    st.session_state["pr"] = ""
    

def promp():
    pr = "Generate a medical based summary of the above text"


questions = []
def generate_questions(text):
    prompt = "Generate questions based on the following text:\n" + text + "\n\n1. "
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=10,
        stop=None,
        temperature=0.5,
    )

    questions = []
    for choice in completions.choices:
        question = choice.text.strip()
        if question:
            questions.append(question)

    return questions

    
    
st.title("Medical Text Summarizer")

input_text = st.text_area(label="Enter full text:", value="", height=250)

st.button(
    "Submit for GPT 3-summarization",
    on_click=summarize,
    kwargs={"prompt": input_text},
)
st.button(
    "Submit for BioGPT-summarization",
    on_click=promp,
    kwargs={"prompt": input_text},
)
st.button(
    "Submit for GPT 3-question generation",
    on_click=generate_questions(input_text),
)

Prompt_field = st.text_area(label="Prompt:", value=st.session_state["pr"], height=100)
summary = st.text_area(label="Summary:", value=st.session_state["summary"], height=100)
questions_field = st.text_area(label="questions:", value = questions, height=100)

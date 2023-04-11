import openai
import streamlit as st

def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    st.session_state["pr"]="Get a medical based summary of this text"
    st.session_state["summary"] = openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=.5,
        max_tokens=1000,
    )["choices"][0]["text"]

def findkeypoints(prompt):
    augmented_prompt = f"Find key points from this text: {prompt}"
    st.session_state["pr"]="Find key points from this text"
    st.session_state["keypoints"] = openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=.5,
        max_tokens=1000,
    )["choices"][0]["text"]
    
def generatequestions(prompt):
    augmented_prompt = f"Generate 5 follow-up questions from this text: {prompt}"
    st.session_state["pr"]="Generate 5 follow-up questions from this text"
    st.session_state["questions"] = openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=.5,
        max_tokens=1000,
    )["choices"][0]["text"]

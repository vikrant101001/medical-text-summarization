import openai
import streamlit as st

def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    st.session_state["summary"] = openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=.5,
        max_tokens=1000,
    )["choices"][0]["text"]
 
def questiongenerate(prompt):
    augmentedb_prompt = "Generate questions based on the following text:\n" + prompt + "\n\n1. "
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=augmentedb_prompt,
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

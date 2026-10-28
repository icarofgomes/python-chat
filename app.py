import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAIError

from tutor.chain import build_chain
from tutor.conversation import ModelError, reply
from tutor.suggestions import SUGGESTIONS

load_dotenv()

st.title("Tutor de Python")

if "messages" not in st.session_state:
    st.session_state.messages = []


def answer(question):
    # O turno atual vai como question. O histórico é o que já aconteceu.
    history = list(st.session_state.messages)
    st.session_state.messages.append({"role": "user", "content": question})
    try:
        if not os.getenv("OPENAI_API_KEY"):
            text = "Coloca a OPENAI_API_KEY no .env."
        else:
            text = reply(history, question, build_chain())
    except (ModelError, OpenAIError):
        text = "Não consegui responder agora."
    st.session_state.messages.append({"role": "assistant", "content": text})


draft = st.session_state.pop("draft", None)
if draft:
    answer(draft)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if not st.session_state.messages:
    st.caption("Sugestões de perguntas")
    for suggestion in SUGGESTIONS:
        if st.button(suggestion):
            st.session_state.draft = suggestion
            st.rerun()

typed = st.chat_input("Pergunte sobre Python")
if typed:
    answer(typed)
    st.rerun()

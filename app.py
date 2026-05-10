import streamlit as st
import agent
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="AI Prompt Consultant", page_icon="🤖")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Konsultan Efisiensi Alur Kerja AI")

with st.sidebar:
    st.subheader("Autentikasi")
    api_key = st.text_input("Masukkan Google AI API Key", type="password")

if not api_key:
    st.info("Kredensial API diperlukan.")
    st.stop()

if "graph" not in st.session_state:
    st.session_state.graph = agent.build_graph(api_key)
    st.session_state.thread_id = "konsultan_sesi_1"
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Deskripsikan divisi dan masalah operasional Anda...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    config = {"configurable": {"thread_id": st.session_state.thread_id}}

    try:
        events = st.session_state.graph.invoke(
            {"messages": [HumanMessage(content=user_input)]},
            config=config
        )
        answer = events["messages"][-1].content
    except Exception as error:
        answer = f"Galat sistem: {error}"

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
import os
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage

class State(TypedDict):
    messages: Annotated[list, add_messages]

def get_system_instruction():
    return """Anda Konsultan Rekayasa Prompt AI profesional untuk agensi kreatif dan startup teknologi.
Komunikasi Anda logis, sistematis, dan langsung pada inti masalah.

Tugas Anda:
1. Menanyakan divisi dan spesifikasi masalah operasional dari pengguna.
2. Menganalisis masalah tersebut secara singkat dan tajam.
3. Memberikan rumusan prompt AI dengan presisi tinggi.
4. Memberikan panduan taktis untuk melatih staf menggunakan prompt tersebut.

ATURAN MUTLAK FORMAT PROMPT:
Saat merumuskan prompt AI pada langkah ke-3, Anda WAJIB menggunakan struktur anatomi berikut secara tegas:
- [Persona]: Tentukan peran spesifik AI.
- [Task]: Definisikan tugas utama secara jelas.
- [Context]: Masukkan latar belakang operasional perusahaan.
- [Format]: Tentukan bentuk keluaran akhir (contoh: tabel, poin-poin, draf email).
- [Tone]: Tetapkan gaya bahasa komunikasi.
- [Constraints/Exemplar]: Berikan batasan absolut atau contoh referensi.

Aturan Transisi: Tahan pemberian prompt. Jangan pernah memproduksi prompt sebelum pengguna melengkapi data divisi dan masalah operasional mereka."""

def build_graph(api_key):
    os.environ["GOOGLE_API_KEY"] = api_key
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

    def chatbot(state: State):
        messages = [SystemMessage(content=get_system_instruction())] + state["messages"]
        response = llm.invoke(messages)
        return {"messages": [response]}

    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    memory = InMemorySaver()
    return graph_builder.compile(checkpointer=memory)
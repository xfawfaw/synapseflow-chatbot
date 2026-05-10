import streamlit as st
import agent
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="SynapseFlow - Chatbot", page_icon="🤖", layout="wide")

# Muat CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Judul SynapseFlow di Kanan Atas
st.markdown('<div class="top-right-title">SynapseFlow</div>', unsafe_allow_html=True)

# Elemen Melayang di Background
st.markdown("""
    <div class="floating-elements">
        <div class="icon" style="top: 10%; left: 5%; animation: float 6s infinite ease-in-out;">📄</div>
        <div class="icon" style="top: 25%; left: 85%; animation: float 8s infinite ease-in-out;">💡</div>
        <div class="icon" style="top: 70%; left: 10%; animation: sway 7s infinite ease-in-out;">📊</div>
        <div class="icon" style="top: 80%; left: 80%; animation: float 5s infinite ease-in-out;">🚀</div>
        <div class="icon" style="top: 40%; left: 15%; animation: float 9s infinite ease-in-out;">📝</div>
        <div class="icon" style="top: 15%; left: 70%; animation: sway 6s infinite ease-in-out;">🧠</div>
        <div class="icon" style="top: 60%; left: 90%; animation: float 7s infinite ease-in-out;">📅</div>
        <div class="icon" style="top: 30%; left: 3%; animation: sway 8s infinite ease-in-out;">🖇️</div>
        <div class="icon" style="top: 50%; left: 50%; animation: float 10s infinite ease-in-out;">📄</div>
        <div class="icon" style="top: 20%; left: 30%; animation: sway 12s infinite ease-in-out;">📄</div>
        <div class="icon" style="top: 85%; left: 40%; animation: float 9s infinite ease-in-out;">📄</div>
        <div class="icon" style="top: 10%; left: 90%; animation: sway 11s infinite ease-in-out;">📄</div>
        <div class="icon" style="top: 65%; left: 25%; animation: float 8s infinite ease-in-out;">📄</div>
        <div class="icon" style="top: 45%; left: 75%; animation: sway 13s infinite ease-in-out;">📄</div>
        <div class="icon" style="top: 5%; left: 45%; animation: float 12s infinite ease-in-out;">📄</div>
        <div class="icon" style="top: 90%; left: 10%; animation: sway 10s infinite ease-in-out;">📄</div>
        <div class="icon" style="top: 35%; left: 60%; animation: float 11s infinite ease-in-out;">📄</div>
        <div class="icon" style="top: 75%; left: 95%; animation: sway 9s infinite ease-in-out;">📄</div>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://img.icons8.com/fluency/100/ffffff/brain.png", width=100)
    st.title("SynapseFlow Hub")
    
    st.subheader("🔑 Autentikasi")
    api_key = st.text_input("Google AI API Key", type="password", placeholder="AIzaSy...")
    
    if api_key:
        st.success("API Key Terpasang!")
    else:
        st.warning("Kredensial API diperlukan untuk memulai.")

    st.divider()
    
    with st.expander("📖 Panduan Penggunaan", expanded=False):
        st.write("""
        1. **Input Masalah:** Jelaskan hambatan operasional atau alur kerja Anda.
        2. **Analisis AI:** SynapseFlow akan menganalisis titik inefisiensi.
        3. **Rekomendasi:** Dapatkan langkah-langkah konkret untuk perbaikan.
        """)
    
    with st.expander("💡 Rekomendasi Prompt", expanded=False):
        st.info("- 'Bagaimana cara mengotomatiskan approval cuti?'")
        st.info("- 'Optimasi alur kerja tim kreatif dengan AI.'")
        st.info("- 'Analisis botleneck di divisi pengadaan.'")

    with st.expander("❓ FAQ", expanded=False):
        st.write("**Apakah data saya aman?**")
        st.caption("Data Anda diproses secara anonim melalui API Google AI.")
        st.write("**Bisakah saya ekspor hasil?**")
        st.caption("Anda dapat menyalin teks langsung dari gelembung chat.")

    st.markdown("---")
    st.caption("v1.2 | Powered by Gemini AI")

if not api_key:
    st.stop()

if "graph" not in st.session_state:
    st.session_state.graph = agent.build_graph(api_key)
    st.session_state.thread_id = "konsultan_sesi_1"
    st.session_state.messages = []

# Container untuk chat agar tidak tertutup elemen floating (meskipun z-index sudah diatur)
chat_container = st.container()

with chat_container:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

user_input = st.chat_input("Deskripsikan divisi dan masalah operasional Anda...")

if user_input:
    # 1. Tampilkan input pengguna
    st.session_state.messages.append({"role": "user", "content": user_input})
    with chat_container:
        with st.chat_message("user"):
            st.markdown(user_input)

    # 2. Persiapkan wadah asisten
    with chat_container:
        with st.chat_message("assistant"):
            thinking_placeholder = st.empty()
            thinking_placeholder.markdown("""
                <div class="thinking-container">
                    <div class="dot"></div>
                    <div class="dot"></div>
                    <div class="dot"></div>
                </div>
            """, unsafe_allow_html=True)

            config = {"configurable": {"thread_id": st.session_state.thread_id}}

            try:
                events = st.session_state.graph.invoke(
                    {"messages": [HumanMessage(content=user_input)]},
                    config=config
                )
                answer = events["messages"][-1].content
            except Exception as error:
                answer = f"Galat sistem: {error}"

            thinking_placeholder.empty()
            st.markdown(answer)

    # Simpan jawaban ke memori
    st.session_state.messages.append({"role": "assistant", "content": answer})

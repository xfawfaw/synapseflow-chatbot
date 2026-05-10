import streamlit as st
import agent

# Konfigurasi Halaman
st.set_page_config(page_title="AI Prompt Consultant", page_icon="🤖")

# Memuat file CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Konsultan Efisiensi Alur Kerja AI")

with st.sidebar:
    st.subheader("Autentikasi")
    api_key = st.text_input("Masukkan Google AI API Key", type="password")

if not api_key:
    st.info("Kredensial API diperlukan untuk memulai sesi diagnostik.")
    st.stop()

# Inisialisasi Memori dan Klien
if "client" not in st.session_state:
    st.session_state.client = agent.init_gemini_client(api_key)
    st.session_state.chat = st.session_state.client.chats.create(
        model="gemini-2.5-flash",
        config=agent.get_chat_config()
    )
    st.session_state.messages = []

# Merender Riwayat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Mengelola Input Pengguna
user_input = st.chat_input("Deskripsikan divisi dan masalah operasional Anda...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
        
    try:
        response = st.session_state.chat.send_message(user_input)
        answer = response.text
    except Exception as error:
        answer = f"Sistem mendeteksi galat: {error}"
        
    with st.chat_message("assistant"):
        st.markdown(answer)
        
    st.session_state.messages.append({"role": "assistant", "content": answer})
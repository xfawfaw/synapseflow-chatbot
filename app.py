import streamlit as st
import agent
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="SynapseFlow - Chatbot", page_icon="🤖", layout="wide")

# Inisialisasi Session State (Sangat Penting: Lakukan di awal agar tidak error di Sidebar)
if "messages" not in st.session_state:
    st.session_state.messages = []
if "thread_id" not in st.session_state:
    st.session_state.thread_id = "konsultan_sesi_1"

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
    st.title("SynapseFlow - Chatbot")
    
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
    
    # Inovasi 3: Live Process Stepper
    st.subheader("📊 Progress Konsultasi")
    
    # Deteksi progress berdasarkan pesan
    all_content = " ".join([m["content"] for m in st.session_state.messages])
    steps = [
        ("🔍 Identifikasi Divisi", "Divisi" in all_content or "divisi" in all_content),
        ("🧠 Analisis Masalah", "Analisis" in all_content or "analisis" in all_content),
        ("✍️ Rumusan Prompt", "[Persona]" in all_content),
        ("📚 Panduan Pelatihan", "Pelatihan" in all_content or "Staf" in all_content or "staf" in all_content)
    ]
    
    for label, completed in steps:
        icon = "✅" if completed else "⏳"
        color = "var(--accent-color)" if completed else "var(--sidebar-text)"
        st.markdown(f'<div style="color: {color}; font-size: 0.9rem; margin-bottom: 5px;">{icon} {label}</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.caption("v1.3 | Powered by Gemini AI")

def highlight_anatomy(text):
    # Inovasi 4: Smart Anatomy Highlighting
    tags = ["[Persona]", "[Task]", "[Context]", "[Format]", "[Tone]", "[Constraints/Exemplar]"]
    for tag in tags:
        text = text.replace(tag, f'<span class="anatomy-tag">{tag}</span>')
    return text

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
            if msg["role"] == "assistant":
                if "---" in msg["content"]:
                    # Inovasi 1: Complexity Badge (Visual Depth Meter)
                    st.markdown('<div class="workflow-badge">Depth: Advanced Analysis</div>', unsafe_allow_html=True)
                # Inovasi 4: Tampilkan dengan Highlighting
                content = highlight_anatomy(msg["content"])
                st.markdown(content, unsafe_allow_html=True)
            else:
                st.markdown(msg["content"])

# Inovasi 2: Interactive Quick-Action Chips
st.markdown('<div style="margin-top: 2rem;"></div>', unsafe_allow_html=True)
cols = st.columns([1, 1, 1, 1])
quick_actions = [
    ("📋 HR Audit", "Analisis inefisiensi di divisi HR kami."),
    ("🚀 Marketing", "Buat prompt untuk optimasi konten marketing."),
    ("🛠️ Operations", "Otomatisasi alur kerja approval inventaris."),
    ("🧠 Brainstorm", "Ide penggunaan AI untuk efisiensi tim.")
]

user_input = st.chat_input("Deskripsikan divisi dan masalah operasional Anda...")

# Handle Quick Actions
for i, (label, prompt) in enumerate(quick_actions):
    if cols[i].button(label, use_container_width=True):
        user_input = prompt

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

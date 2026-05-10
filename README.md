# 🤖 SynapseFlow - Chatbot
### *Elevating Corporate Workflow Efficiency through Precision AI Prompt Engineering*

**SynapseFlow** adalah asisten AI Konsultan Rekayasa Prompt (*Prompt Engineering*) yang dirancang khusus untuk agensi kreatif, media, dan rintisan teknologi (*tech startups*). Dibangun dengan arsitektur **LangGraph** dan ditenagai oleh **Gemini 2.5 Flash**, chatbot ini bertindak sebagai pakar diagnostik yang membedah inefisiensi operasional dan merumuskan instruksi AI yang presisi.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-2D3748?style=for-the-badge&logo=langchain&logoColor=white)

---

## 🚀 Fitur Utama

* **Diagnostic-First Approach**: Chatbot tidak langsung memberikan jawaban. Ia akan melakukan diagnosis terstruktur terhadap divisi dan hambatan operasional Anda untuk memastikan solusi yang tepat sasaran.
* **Standardized Prompt Anatomy**: Setiap solusi yang dihasilkan mengikuti struktur anatomi prompt profesional:
    * `[Persona]`, `[Task]`, `[Context]`, `[Format]`, `[Tone]`, dan `[Constraints/Exemplar]`.
* **SaaS Minimalist Interface**: Desain antarmuka modern dengan skema warna *Moving Gradient* (Cyan, Magenta, Navy) dan efek *Glassmorphism*.
* **Intelligent Memory**: Berkat integrasi LangGraph `StateGraph`, chatbot mampu mengingat konteks diagnostik selama sesi berlangsung tanpa kehilangan jejak informasi.
* **Interactive UI Components**: Dilengkapi dengan animasi *thinking indicator* dan transformasi kolom input yang atraktif untuk pengalaman pengguna yang lebih "hidup".

---

## 🛠️ Arsitektur Teknis

Aplikasi ini menggabungkan beberapa teknologi canggih:
1.  **Framework Antarmuka**: [Streamlit](https://streamlit.io/) untuk pembangunan web app yang cepat dan interaktif.
2.  **Orkestrasi AI**: [LangGraph](https://langchain-ai.github.io/langgraph/) untuk mengelola alur logika agen dan memori sesi.
3.  **Model Bahasa**: [Google Gemini 2.5 Flash](https://ai.google.dev/) melalui SDK `google-genai` untuk penalaran logis tingkat tinggi.
4.  **Styling**: Custom CSS murni untuk animasi dinamis dan branding *SynapseFlow*.

---

## 📦 Instalasi & Penggunaan Lokal

1. **Clone Repositori**
   ```bash
   git clone [https://github.com/USERNAME_ANDA/synapseflow-chatbot.git](https://github.com/USERNAME_ANDA/synapseflow-chatbot.git)
   cd synapseflow-chatbot
Setup Lingkungan Virtual

Bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Mac/Linux
Instal Dependensi

Bash
pip install -r requirements.txt
Jalankan Aplikasi

Bash
streamlit run app.py
💡 Cara Penggunaan
Dapatkan Google AI API Key dari Google AI Studio.

Masukkan kunci API pada sidebar aplikasi.

Deskripsikan divisi Anda (misal: Marketing Agency) dan masalah yang ingin diefisiensikan (misal: Pembuatan caption media sosial yang memakan waktu terlalu lama).

Ikuti instruksi diagnostik dari SynapseFlow hingga Anda mendapatkan Optimal AI Prompt yang siap digunakan.

👤 Author
Bintang Fergiawan
Information Systems Student @ UPN "Veteran" Yogyakarta
AI Enthusiast

Proyek ini disusun sebagai Final Project untuk program "LLM-Based Tools and Gemini API Integration for Data Scientists" oleh Hacktiv8.


### Tips Tambahan untuk GitHub:
1.  **Tangkapan Layar**: Pastikan Anda mengunggah file gambar hasil *screenshot* ke repositori Anda (misalnya di folder `img/`), lalu ganti baris teks di bawah judul dengan tag gambar: `![SynapseFlow UI](img/screenshot.png)`.
2.  **Link Live Demo**: Tambahkan baris `[🔗 Live Demo di Streamlit Cloud](https://synapseflow-chatbot.streamlit.app/)` tepat di bawah *tagline* agar penilai bisa langsung mencoba aplikasi Anda.
from google import genai
from google.genai import types

def init_gemini_client(api_key):
    return genai.Client(api_key=api_key)

def get_system_instruction():
    return """
    Anda adalah Konsultan Rekayasa Prompt AI untuk agensi kreatif dan startup teknologi.
    Komunikasi Anda murni logis, sistematis, dan langsung pada inti masalah.
    Tugas Anda:
    1. Tanya divisi dan masalah efisiensi pengguna.
    2. Analisis masalah tersebut.
    3. Berikan rumusan prompt AI presisi tinggi dan cara melatih staf menggunakannya.
    Jangan gunakan metafora. Hindari kalimat pasif.
    """

def get_chat_config():
    return types.GenerateContentConfig(
        system_instruction=get_system_instruction(),
        temperature=0.3, # Nilai rendah menjaga konsistensi dan kelogisan jawaban
        top_p=0.9,
    )
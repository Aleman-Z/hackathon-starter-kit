import streamlit as st
import requests

st.set_page_config(page_title="Spotify para aprender", layout="centered")

st.title("📘 Spotify para aprender")
st.markdown("Escribe un tema de interés (por ejemplo, 'CRISPR') y recibe un resumen educativo de aproximadamente 5 minutos de lectura.")

# Inicializar estado
if "full_text" not in st.session_state:
    st.session_state.full_text = ""

# Entrada
topic = st.text_input("📚 Tema que quieres aprender:", value="CRISPR")

if st.button("Generar resumen"):
    with st.spinner("Generando..."):
        try:
            response = requests.post("http://127.0.0.1:8000/generate-text", json={"topic": topic})
            if response.status_code == 200:
                result = response.json()
                st.session_state.full_text = result["text"]
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

# Mostrar texto completo
if st.session_state.full_text:
    st.markdown("### 🧠 Resumen generado:")
    st.text_area("", value=st.session_state.full_text, height=1000)

    if st.button("🔊 Generar audio con ElevenLabs"):
        with st.spinner("Generando audio..."):
            try:
                audio_response = requests.post(
                    "http://127.0.0.1:8000/generate-audio",
                    json={"text": st.session_state.full_text}
                )
                if audio_response.status_code == 200:
                    audio_data = audio_response.json().get("audio_base64", "")
                    if audio_data:
                        st.audio(f"data:audio/mp3;base64,{audio_data}", format="audio/mp3")
                    else:
                        st.error("No se recibió audio válido.")
                else:
                    st.error(f"Error al generar audio: {audio_response.text}")
            except Exception as e:
                st.error(f"Ocurrió un error al generar el audio: {e}")


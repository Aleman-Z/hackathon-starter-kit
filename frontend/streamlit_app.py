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

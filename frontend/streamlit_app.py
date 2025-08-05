import streamlit as st
import requests

st.set_page_config(page_title="Spotify para aprender", layout="centered")

st.title("📘 Spotify para aprender")
st.markdown("Escribe un tema de interés (por ejemplo, 'CRISPR') y recibe un resumen educativo de aproximadamente 5 minutos de lectura.")

# --- Inicializar estado si no existe ---
if "full_text" not in st.session_state:
    st.session_state.full_text = ""
if "page" not in st.session_state:
    st.session_state.page = 0
if "page_size" not in st.session_state:
    st.session_state.page_size = 5000

# --- Entrada de usuario ---
topic = st.text_input("📚 Tema que quieres aprender:", value="CRISPR")

if st.button("Generar resumen"):
    with st.spinner("Generando..."):
        try:
            response = requests.post("http://127.0.0.1:8000/generate-text", json={"topic": topic})
            if response.status_code == 200:
                result = response.json()
                st.session_state.full_text = result["text"]
                st.session_state.page = 0
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

# --- Mostrar texto paginado ---
if st.session_state.full_text:
    total_pages = (len(st.session_state.full_text) + st.session_state.page_size - 1) // st.session_state.page_size
    start = st.session_state.page * st.session_state.page_size
    end = start + st.session_state.page_size
    page_text = st.session_state.full_text[start:end]

    st.markdown(f"**Página {st.session_state.page + 1} de {total_pages}**")
    st.text_area("🧠 Resumen generado:", value=page_text, height=400)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Anterior"):
            if st.session_state.page > 0:
                st.session_state.page -= 1
                st.experimental_rerun()
    with col2:
        if st.button("Siguiente ➡️"):
            if st.session_state.page < total_pages - 1:
                st.session_state.page += 1
                st.experimental_rerun()

import streamlit as st
import requests

st.set_page_config(page_title="Spotify para aprender", layout="centered")

st.title("📘 Spotify para aprender")
st.markdown("Escribe un tema de interés (por ejemplo, 'CRISPR') y recibe un resumen educativo de aproximadamente 5 minutos de lectura.")

# Initialize session state
if "full_text" not in st.session_state:
    st.session_state.full_text = ""
if "chunks" not in st.session_state:
    st.session_state.chunks = []

topic = st.text_input("📚 Tema que quieres aprender:", value="CRISPR")

if st.button("Generar resumen"):
    with st.spinner("Generando..."):
        try:
            response = requests.post("http://127.0.0.1:8000/generate-text", json={"topic": topic})
            if response.status_code == 200:
                result = response.json()
                full_text = result["text"]

                # Split into 5000-char chunks
                st.session_state.chunks = [full_text[i:i+5000] for i in range(0, len(full_text), 5000)]
                st.session_state.full_text = full_text
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

# Display if text is loaded
if st.session_state.chunks:
    total_pages = len(st.session_state.chunks)
    selected_page = st.selectbox("Selecciona la página:", list(range(1, total_pages + 1))) - 1
    st.markdown(f"**Página {selected_page + 1} de {total_pages}**")
    st.text_area("🧠 Resumen generado:", value=st.session_state.chunks[selected_page], height=500)

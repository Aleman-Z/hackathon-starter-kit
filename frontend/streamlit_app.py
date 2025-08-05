import streamlit as st
import requests

st.set_page_config(page_title="Spotify para aprender", layout="centered")

st.title("📘 Spotify para aprender")
st.markdown("Escribe un tema de interés (por ejemplo, 'CRISPR') y recibe un resumen educativo de aproximadamente 5 minutos de lectura.")

topic = st.text_input("📚 Tema que quieres aprender:", value="CRISPR")

if st.button("Generar resumen"):
    with st.spinner("Generando..."):
        try:
            response = requests.post("http://127.0.0.1:8000/generate-text", json={"topic": topic})

            if response.status_code == 200:
                result = response.json()
                full_text = result["text"]
                page_size = 5000
            
                # Session state to track current page
                if "page" not in st.session_state:
                    st.session_state.page = 0
            
                total_pages = (len(full_text) + page_size - 1) // page_size
            
                cols = st.columns([1, 3, 1])
                with cols[0]:
                    if st.button("⬅️ Anterior") and st.session_state.page > 0:
                        st.session_state.page -= 1
                with cols[2]:
                    if st.button("Siguiente ➡️") and st.session_state.page < total_pages - 1:
                        st.session_state.page += 1
            
                start = st.session_state.page * page_size
                end = start + page_size
                page_text = full_text[start:end]
            
                st.markdown(f"**Página {st.session_state.page + 1} de {total_pages}**")
                st.text_area("", value=page_text, height=400)


            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")


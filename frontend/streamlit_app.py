import streamlit as st
import requests

st.set_page_config(page_title="Code Generator with Mistral", layout="centered")

st.title("💡 Mistral Code Generator")
st.markdown("Escribe el inicio de una función en Python y genera el resto usando el modelo `codestral-2405` vía FastAPI backend.")

prompt = st.text_area("✍️ Escribe tu prompt:", value="def fibonacci(n):", height=150)

if st.button("Generar código"):
    with st.spinner("Generando..."):
        try:
            response = requests.post("http://127.0.0.1:8000/generate-code", json={"prompt": prompt})
            if response.status_code == 200:
                result = response.json()
                st.code(result["generated_code"], language="python")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

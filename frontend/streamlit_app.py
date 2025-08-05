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
            
                st.markdown("### 🧠 Resumen generado:")
            
                # ✅ Custom scrollable HTML container
                st.components.v1.html(f"""
                    <div style="height:800px; overflow-y:scroll; padding:1em; border:1px solid #ddd; background-color:#fefefe; font-family:Arial; white-space:pre-wrap;">
                        {full_text}
                    </div>
                """, height=820)

            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")


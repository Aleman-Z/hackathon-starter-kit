import streamlit as st
import base64

# ============================================================================
# CONFIGURACIÓN DE PÁGINA
# ============================================================================

st.set_page_config(
    page_title="Spotify for Learning",
    page_icon="logo2.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ocultar elementos de Streamlit y ajustar para ancho completo
# Sale una barra blanca por default esta parte la oculta
st.markdown("""
    <style>
    .stApp {
        background-color: #443D44;
        color: white;
    }
    #MainMenu, header, footer {
        visibility: hidden;
    }
    
    /* Eliminar padding del container principal */
    .block-container {
        padding-top: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: none;
    }
    
    /* Eliminar márgenes del contenedor principal */
    .main .block-container {
        padding-top: 0rem;
    }
    </style>
""", unsafe_allow_html=True)
# si mueven esto ya no se ven las imagenes 
# Función para convertir imagen local a base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            b64_string = base64.b64encode(img_file.read()).decode()
            return f"data:image/png;base64,{b64_string}"
    except FileNotFoundError:
        # Placeholder si no encuentra la imagen
        return "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgiIGhlaWdodD0iNDgiIHZpZXdCb3g9IjAgMCA0OCA0OCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMjQiIGN5PSIyNCIgcj0iMjAiIGZpbGw9IndoaXRlIiBmaWxsLW9wYWNpdHk9IjAuMiIvPgo8cGF0aCBkPSJNMzAgMThMMTggMzBNMTggMThMMzAgMzAiIHN0cm9rZT0id2hpdGUiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+Cjwvc3ZnPgo="

logo_base64 = get_base64_image("logo.png")

# Navbar 
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@700&display=swap');

    .navbar-custom {{
        width: 100vw;
        height: 80px;
        background: linear-gradient(90deg, #087238 0%, #CC18C0 100%);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 20px;
        box-sizing: border-box;
        margin-left: calc(-50vw + 50%);
        margin-right: calc(-50vw + 50%);
        position: relative;
        z-index: 1000;
    }}

    .navbar-left {{
        display: flex;
        align-items: center;
        gap: 15px;
        color: white;
        font-family: 'Instrument Sans', sans-serif;
        font-size: 24px;
        font-weight: 700;
        white-space: nowrap;
    }}

    .navbar-logo {{
        height: 48px;
        width: auto;
        filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.1));
    }}

    .navbar-dots {{
        display: flex;
        align-items: center;
        gap: 5px;
        cursor: pointer;
        padding: 8px;
        border-radius: 15px;
        transition: background-color 0.2s ease;
    }}

    .navbar-dots:hover {{
        background-color: rgba(255, 255, 255, 0.1);
    }}

    .dot {{
        height: 8px;
        width: 8px;
        background-color: white;
        border-radius: 50%;
        display: inline-block;
        transition: transform 0.2s ease;
    }}

    .navbar-dots:hover .dot {{
        transform: scale(1.1);
    }}

    /* Responsividad para móviles */
    @media screen and (max-width: 480px) {{
        .navbar-custom {{
            padding: 0 15px;
            height: 70px;
        }}
        
        .navbar-left {{
            font-size: 16px;
            gap: 8px;
        }}
        
        .navbar-logo {{
            height: 32px;
        }}
        
        .navbar-dots {{
            gap: 3px;
            padding: 6px;
        }}
        
        .dot {{
            height: 6px;
            width: 6px;
        }}
    }}

    /* Responsividad para tablets */
    @media screen and (min-width: 481px) and (max-width: 768px) {{
        .navbar-custom {{
            padding: 0 20px;
            height: 75px;
        }}
        
        .navbar-left {{
            font-size: 20px;
            gap: 12px;
        }}
        
        .navbar-logo {{
            height: 40px;
        }}
        
        .dot {{
            height: 7px;
            width: 7px;
        }}
    }}

    /* Responsividad para pantallas medianas */
    @media screen and (min-width: 769px) and (max-width: 1024px) {{
        .navbar-custom {{
            padding: 0 25px;
        }}
        
        .navbar-left {{
            font-size: 22px;
            gap: 14px;
        }}
        
        .navbar-logo {{
            height: 44px;
        }}
    }}

    /* Responsividad para pantallas grandes */
    @media screen and (min-width: 1025px) and (max-width: 1440px) {{
        .navbar-custom {{
            padding: 0 30px;
        }}
        
        .navbar-left {{
            font-size: 24px;
            gap: 15px;
        }}
        
        .navbar-logo {{
            height: 48px;
        }}
    }}

    /* Responsividad para pantallas extra grandes */
    @media screen and (min-width: 1441px) {{
        .navbar-custom {{
            padding: 0 40px;
        }}
        
        .navbar-left {{
            font-size: 26px;
            gap: 18px;
        }}
        
        .navbar-logo {{
            height: 52px;
        }}
        
        .dot {{
            height: 9px;
            width: 9px;
        }}
    }}

    /* Para texto muy largo en móviles */
    @media screen and (max-width: 320px) {{
        .navbar-left {{
            font-size: 14px;
            gap: 6px;
        }}
        
        .navbar-logo {{
            height: 28px;
        }}
    }}
    </style>

    <div class="navbar-custom">
        <div class="navbar-left">
            Spotify for learning
            <img src="{logo_base64}" class="navbar-logo" alt="Logo">
        </div>
        <div class="navbar-dots">
            <span class="dot"></span>
            <span class="dot"></span>
            <span class="dot"></span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ============================================================================
# FUNCIONALIDAD DE RESUMEN Y AUDIO
# ============================================================================

# Variables de estado
if 'resumen_generado' not in st.session_state:
    st.session_state.resumen_generado = False
if 'texto_resumen' not in st.session_state:
    st.session_state.texto_resumen = ""
if 'audio_generado' not in st.session_state:
    st.session_state.audio_generado = False
if 'audio_path' not in st.session_state:
    st.session_state.audio_path = None

# Función para generar resumen (aquí pueden hacer la magia (va la API y el back)
# Texto de ejemplo 
def generar_resumen(tema):
    resumen_ejemplo = f"""**{tema}**: Una introducción completa

{tema} es un tema fascinante que abarca múltiples aspectos y aplicaciones en el mundo moderno. 

**Conceptos clave:**
• Definición y origen del tema
• Aplicaciones prácticas en la vida cotidiana  
• Impacto en diferentes industrias
• Desarrollos futuros y tendencias

**¿Por qué es importante?**
El estudio de {tema} nos permite comprender mejor cómo funciona el mundo que nos rodea y cómo podemos aplicar estos conocimientos para resolver problemas reales.

**Aplicaciones prácticas:**
Este conocimiento puede aplicarse en campos como la tecnología, medicina, educación y muchas otras áreas que afectan nuestra vida diaria.

**Conclusión:**
{tema} representa una oportunidad única para expandir nuestro conocimiento y desarrollar habilidades que serán valiosas en el futuro."""
    return resumen_ejemplo

# Función para generar audio con Eleven Labs (aquí integran la API real)
def generar_audio_eleven_labs(texto):
    import time
    time.sleep(2)  # Simular procesamiento
    return "audio_generado.mp3"  # Retorna la ruta del audio generado

# Función para formatear HTML
def formatear_resumen_html(texto):
    texto_formateado = texto.replace('**', '<strong>')
    texto_formateado = texto_formateado.replace('</strong><strong>', '')
    texto_formateado = texto_formateado.replace('• ', '• ')
    texto_formateado = texto_formateado.replace('\n', '<br>')
    return texto_formateado

# ESTILOS PRINCIPALES - Para los elementos despleglables si lo mueven ya no se ve bonix
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&display=swap');

/* SOLUCIÓN PARA REDUCIR ESPACIADO ENTRE ELEMENTOS DE STREAMLIT */
[data-testid=stVerticalBlock] {
    gap: 0rem !important;
}

[data-testid=stVerticalBlock] > div {
    gap: 0rem !important;
}

/* ELIMINAR ESPACIADO EN CONTENEDORES */
[data-testid=stVerticalBlockBorderWrapper] {
    gap: 0rem !important;
}

/* REDUCIR MÁRGENES DE ELEMENTOS ESPECÍFICOS */
.stMarkdown {
    margin-bottom: 0rem !important;
}

/* PERSONALIZAR TÍTULO CON ST.WRITE */
.custom-title {
    color: white;
    font-size: 35px;
    font-family: 'Instrument Sans', sans-serif;
    font-weight: 500;
    text-align: center;
    margin-top: 20px !important;
    margin-bottom: 0px !important;
    padding-top: 0px !important;
    padding-bottom: 0px !important;
}

/* PERSONALIZAR SUBTÍTULO CON ST.WRITE */
.custom-subtitle {
    text-align: center;
    color: #EDEDED;
    font-size: 24px;
    font-family: 'Instrument Sans', sans-serif;
    font-weight: 700;
    margin-top: 0px !important;
    margin-bottom: 0px !important;
    padding-top: 0px !important;
    padding-bottom: 0px !important;
}

/* ESTILOS PARA FUNCIONALIDAD */
.resumen-container {
    margin: 40px 20% 30px 20%;
    text-align: left;
}

.resumen-box {
    width: 100%;
    min-height: 200px;
    max-height: 600px;
    background-color: #52506B;
    border: 2px solid #764084;
    border-radius: 16px;
    padding: 24px;
    font-family: 'Instrument Sans', sans-serif;
    font-size: 16px;
    color: #A8A8A8;
    box-sizing: border-box;
    overflow-y: auto;
    line-height: 1.6;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.resumen-box strong {
    color: #EDEDED;
}

.audio-container {
    margin: 30px 20% 20px 20%;
    text-align: center;
}

.audio-player {
    width: 100%;
    max-width: 500px;
    margin: 0 auto 20px auto;
    background-color: #E5E5E5;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.audio-player audio {
    width: 100%;
    background-color: #F5F5F5;
    border-radius: 8px;
}

/* ESTILOS PARA ELEMENTOS DE STREAMLIT */
.stTextArea {
    margin: 15px 20% 30px 20% !important; /* Margen mínimo superior */
}

.stTextArea > div > div > textarea {
    background-color: #52506B !important;
    border: 2px solid transparent !important;
    border-radius: 16px !important;
    color: white !important;
    font-family: 'Instrument Sans', sans-serif !important;
    font-size: 16px !important;
    transition: all 0.3s ease !important;
    padding: 20px 24px !important;
    height: 80px !important;
    width: 100% !important;
}

.stTextArea > div > div > textarea:focus {
    border-color: #764084 !important;
    box-shadow: 0 0 0 3px rgba(118, 64, 132, 0.2) !important;
    background-color: #5A5770 !important;
}

.stTextArea > div > div > textarea::placeholder {
    color: #A8A8A8 !important;
}

.stButton {
    display: flex !important;
    justify-content: center !important;
    margin-bottom: 20px !important;
}

.stButton > button {
    background: linear-gradient(135deg, #764084 0%, #8B4A9C 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 16px 32px !important;
    font-family: 'Instrument Sans', sans-serif !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 16px rgba(118, 64, 132, 0.3) !important;
    width: auto !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #8B4A9C 0%, #A055B8 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(118, 64, 132, 0.4) !important;
}

/* Estilos específicos para botón de audio - ROSA DE SPOTIFY */
button[key="generar_audio"] {
    background: linear-gradient(135deg, #CC18C0 0%, #E021D8 100%) !important;
    box-shadow: 0 4px 16px rgba(204, 24, 192, 0.3) !important;
}

button[key="generar_audio"]:hover {
    background: linear-gradient(135deg, #E021D8 0%, #F024E6 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(204, 24, 192, 0.4) !important;
}

/* Estilos específicos para botón de descarga - VERDE */
button[key="descargar_audio"] {
    background: linear-gradient(135deg, #087238 0%, #0A8F43 100%) !important;
    box-shadow: 0 4px 16px rgba(8, 114, 56, 0.3) !important;
}

button[key="descargar_audio"]:hover {
    background: linear-gradient(135deg, #0A8F43 0%, #0CAD4F 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(8, 114, 56, 0.4) !important;
}

/* FOOTER - si lo quieren modifica es esta linea */ 
.footer {
    width: 100vw;
    margin-left: calc(-50vw + 50%);
    margin-right: calc(-50vw + 50%);
    background-color: #2D2D2D;
    color: #CCCCCC;
    text-align: center;
    padding: 20px 0;
    font-family: 'Instrument Sans', sans-serif;
    font-size: 14px;
    font-weight: 400;
    margin-top: 60px;
    border-top: 1px solid #4A4A4A;
}

@media screen and (max-width: 768px) {
    .stTextArea, .resumen-container, .audio-container {
        margin-left: 10% !important;
        margin-right: 10% !important;
    }
    .stTextArea {
        margin-top: 10px !important;
    }
    .custom-title {
        font-size: 32px;
        margin-top: 15px !important;
    }
    .custom-subtitle {
        font-size: 20px;
    }
    .stTextArea > div > div > textarea {
        height: 70px !important;
        font-size: 15px !important;
    }
    .stButton > button {
        padding: 14px 28px !important;
        font-size: 15px !important;
    }
    .footer {
        font-size: 12px;
        padding: 15px 10px;
        margin-top: 40px;
    }
}

@media screen and (max-width: 480px) {
    .stTextArea, .resumen-container, .audio-container {
        margin-left: 5% !important;
        margin-right: 5% !important;
    }
    .stTextArea {
        margin-top: 10px !important;
    }
    .custom-title {
        font-size: 28px;
        margin-top: 10px !important;
    }
    .custom-subtitle {
        font-size: 18px;
    }
    .stTextArea > div > div > textarea {
        height: 60px !important;
        font-size: 14px !important;
    }
    .footer {
        font-size: 11px;
        padding: 12px 5px;
        margin-top: 30px;
    }
}
</style>
""", unsafe_allow_html=True)

# CONTENIDO PRINCIPAL 
st.write('<h1 class="custom-title">                      </h1>', unsafe_allow_html=True)
st.write('<h1 class="custom-title">¿Qué aprenderemos hoy?</h1>', unsafe_allow_html=True)
st.write('<h1 class="custom-title">                      </h1>', unsafe_allow_html=True)


st.write('''<p class="custom-subtitle">
Escribe cualquier tema que te interese y obtén un resumen educativo personalizado.<br>
Por ejemplo: CRISPR, Machine Learning, Historia del Arte...
</p>''', unsafe_allow_html=True)
st.write('<h1 class="custom-title">                      </h1>', unsafe_allow_html=True)
# ELEMENTOS FUNCIONALES DE STREAMLIT - Posicionados inmediatamente después
tema_input = st.text_area(
    "",
    placeholder="Escribe tu tema de interés aquí... ej: Fotosíntesis, Revolución Francesa, Programación Python",
    height=80,
    key="tema_input",
    label_visibility="collapsed"
)

# Botón para generar resumen
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("⭐ Generar resumen", key="generar_resumen"):
        if tema_input.strip():
            with st.spinner("Generando resumen..."):
                st.session_state.texto_resumen = generar_resumen(tema_input)
                st.session_state.resumen_generado = True
                st.session_state.audio_generado = False
                st.rerun()
        else:
            st.warning("Por favor, escribe un tema para generar el resumen.")

# Mostrar área de resumen si se ha generado
if st.session_state.resumen_generado:
    texto_html = formatear_resumen_html(st.session_state.texto_resumen)
    
    st.markdown(f"""
    <div class="resumen-container">
        <div class="resumen-box">
            {texto_html}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Botón para generar audio
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🎵 Generar audio", key="generar_audio"):
            with st.spinner("Generando audio con Eleven Labs..."):
                audio_path = generar_audio_eleven_labs(st.session_state.texto_resumen)
                st.session_state.audio_path = audio_path
                st.session_state.audio_generado = True
                st.rerun()

# Mostrar reproductor de audio si se ha generado
if st.session_state.audio_generado and st.session_state.audio_path:
    st.markdown(f"""
    <div class="audio-container">
        <div class="audio-player">
            <audio controls>
                <source src="{st.session_state.audio_path}" type="audio/mpeg">
                Tu navegador no soporta el elemento de audio.
            </audio>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Botón para descargar audio
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📥 Descargar audio", key="descargar_audio"):
            st.success("¡Audio descargado exitosamente!")

# FOOTER
st.write('<div class="footer">Todos los derechos reservados TEAM MEXICO GLOBAL IA HACKATHON</div>', 
         unsafe_allow_html=True)

#Nota probe la responsividad funciono pero no esta demas que se verifique en diferentes dispositivos
# Nota: La responsividad se ha probado en dispositivos móviles y tablets, pero es recomendable verificar
# Código creado con IA (Inteligencia y ansiedad ) y un poco de claude y varios videos de youtube 
# Esve_bavi
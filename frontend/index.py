import streamlit as st
import time

# ============================================================================
# CONFIGURACIÓN DE PÁGINA
# ============================================================================
st.set_page_config(
    page_title="Spotify for Learning",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# IMPORTACIÓN DE STYLABLE CONTAINER
# ============================================================================
try:
    from streamlit_extras.stylable_container import stylable_container
    STYLABLE_AVAILABLE = True
except ImportError:
    st.error("⚠️ Para el diseño completo, instala: pip install streamlit-extras")
    STYLABLE_AVAILABLE = False

# ============================================================================
# ESTADO DE SESIÓN
# ============================================================================
if 'learning_list' not in st.session_state:
    st.session_state.learning_list = []
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
if 'timer_start' not in st.session_state:
    st.session_state.timer_start = 0
if 'timer_duration' not in st.session_state:
    st.session_state.timer_duration = 0
if 'timer_minutes' not in st.session_state:
    st.session_state.timer_minutes = ''
if 'show_timer_options' not in st.session_state:
    st.session_state.show_timer_options = False
if 'menu_active' not in st.session_state:
    st.session_state.menu_active = False

# ============================================================================
# ESTILOS CSS COMPLETOS - NAVBAR FIJO ARRIBA
# ============================================================================
st.markdown("""
<style>
    /* ===== IMPORTAR FUENTES E ICONOS ===== */
    @import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
    
    /* ===== RESET COMPLETO DE STREAMLIT ===== */
    .stApp {
        background-color: #443D44;
        color: white;
    }
    
    /* Ocultar elementos de Streamlit */
    .stApp > header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    .stDecoration {display: none;}
    .stToolbar {display: none;}
    [data-testid="stHeader"] {
        visibility: hidden;
        height: 0px;
    }
    
    /* ELIMINAR COMPLETAMENTE EL PADDING SUPERIOR */
    .main .block-container {
        padding-top: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        padding-bottom: 0 !important;
        margin-top: 0 !important;
        max-width: 100% !important;
    }
    
    /* FORZAR EL CONTENIDO A LA PARTE SUPERIOR */
    .stApp > div {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    
    /* ===== NAVBAR COMPLETAMENTE FIJO ARRIBA ===== */
    .navbar-full {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 129px;
        background: linear-gradient(90deg, #087238 0%, #CC18C0 100%);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 4%;
        box-sizing: border-box;
        z-index: 9999;
        margin: 0;
    }
    
    .navbar-left {
        display: flex;
        align-items: center;
        gap: 20px;
    }
    
    .navbar-title {
        color: white;
        font-size: 24px;
        font-family: 'Instrument Sans', sans-serif;
        font-weight: 700;
        margin: 0;
    }
    
    /* Logo de Spotify exacto */
    .spotify-icon {
        position: relative;
        width: 55px;
        height: 55px;
    }
    
    .spotify-circle {
        width: 45.83px;
        height: 45.83px;
        background: white;
        border-radius: 50%;
        position: absolute;
        top: 4.58px;
        left: 4.58px;
    }
    
    .spotify-overlay {
        width: 34px;
        height: 34px;
        background: #FFD6FC;
        border-radius: 50%;
        position: absolute;
        top: 10px;
        left: 26px;
        transform: rotate(-30deg);
    }
    
    .menu-dots {
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        border-radius: 50%;
        transition: all 0.3s ease;
        color: white;
        font-size: 20px;
    }
    
    .menu-dots:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    .menu-dots.active {
        background-color: #764084;
    }
    
    /* ===== CONTENIDO PRINCIPAL CON MARGIN-TOP ===== */
    .main-container {
        margin-top: 129px;
        padding: 2rem 4%;
        width: 100%;
        box-sizing: border-box;
    }
    
    .main-title {
        text-align: center;
        font-size: 40px;
        font-family: 'Instrument Sans', sans-serif;
        font-weight: 700;
        color: white;
        margin: 2rem 0;
    }
    
    /* ===== INPUT DE BÚSQUEDA MEJORADO CON TIMER INTEGRADO ===== */
    .search-container {
        max-width: 800px;
        margin: 0 auto 3rem auto;
        position: relative;
    }
    
    .search-input-wrapper {
        position: relative;
        display: flex;
        align-items: center;
    }
    
    .stTextInput > div > div > input {
        background: #52506B !important;
        border: none !important;
        border-radius: 30px !important;
        color: #EDEDED !important;
        font-size: 24px !important;
        font-family: 'Instrument Sans', sans-serif !important;
        padding: 36px 120px 36px 33px !important;
        height: 130px !important;
        box-sizing: border-box !important;
        width: 100% !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #EDEDED !important;
        opacity: 0.8 !important;
    }
    
    .stTextInput > label {
        display: none !important;
    }
    
    /* ===== ÍCONO DEL RELOJ DENTRO DEL INPUT ===== */
    .clock-icon-container {
        position: absolute;
        right: 20px;
        top: 50%;
        transform: translateY(-50%);
        z-index: 10;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .clock-icon {
        width: 40px;
        height: 40px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #EDEDED;
        font-size: 18px;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    .clock-icon:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: scale(1.1);
    }
    
    .timer-input {
        width: 60px;
        height: 35px;
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 15px !important;
        color: #EDEDED !important;
        font-size: 14px !important;
        text-align: center !important;
        font-family: 'Instrument Sans', sans-serif !important;
    }
    
    .timer-input::placeholder {
        color: rgba(237, 237, 237, 0.6) !important;
    }
    
    /* ===== BOTONES DE ACCIÓN CON ICONOS ===== */
    .action-buttons {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .action-btn-styled {
        background: #764084 !important;
        color: white !important;
        border: none !important;
        border-radius: 40px !important;
        height: 66px !important;
        padding: 0 2rem !important;
        font-size: 18px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 700 !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        align-items: center !important;
        gap: 0.5rem !important;
        cursor: pointer !important;
    }
    
    .action-btn-styled:hover {
        background: #8a4d96 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(118, 64, 132, 0.4) !important;
    }
    
    /* ===== LAYOUT PRINCIPAL ===== */
    .content-layout {
        display: flex;
        gap: 2rem;
        align-items: flex-start;
    }
    
    /* ===== LISTA DE APRENDIZAJE ESTILIZADA ===== */
    .learning-list-sidebar {
        width: 350px;
        min-width: 350px;
        background: linear-gradient(90deg, rgba(8.35, 114.26, 56.01, 0.20) 0%, rgba(218.22, 192.83, 216.53, 0.20) 100%);
        border-radius: 20px;
        padding: 2rem;
        backdrop-filter: blur(10px);
        min-height: 500px;
    }
    
    .learning-list-title {
        color: #764084;
        font-size: 24px;
        font-family: 'Instrument Sans', sans-serif;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }
    
    .learning-item-card {
        background: rgba(68, 61, 68, 0.8);
        border-radius: 20px;
        padding: 1rem 1.5rem;
        margin: 1rem 0;
        font-family: 'Instrument Sans', sans-serif;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: all 0.3s ease;
    }
    
    .learning-item-card:hover {
        background: rgba(68, 61, 68, 0.9);
        transform: translateY(-2px);
    }
    
    .remove-icon {
        color: rgba(255, 255, 255, 0.7);
        cursor: pointer;
        padding: 0.5rem;
        border-radius: 50%;
        transition: all 0.3s ease;
    }
    
    .remove-icon:hover {
        background: rgba(255, 0, 0, 0.2);
        color: #ff4444;
    }
    
    .empty-list-message {
        color: rgba(255, 255, 255, 0.6);
        text-align: center;
        font-family: 'Instrument Sans', sans-serif;
        padding: 3rem 1rem;
        font-style: italic;
        border: 2px dashed rgba(118, 64, 132, 0.3);
        border-radius: 15px;
        margin-top: 1rem;
    }
    
    /* ===== CONTENIDO DE ITEMS ===== */
    .items-content {
        flex: 1;
    }
    
    .recommendations-title {
        font-size: 24px;
        font-family: 'Instrument Sans', sans-serif;
        font-weight: 700;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .items-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        max-width: 800px;
        margin: 0 auto;
    }
    
    .item-card {
        background: linear-gradient(90deg, #443D44 0%, rgba(255, 255, 255, 0.50) 100%);
        border-radius: 20px;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 1.5rem 0 3rem;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .item-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    .item-text {
        color: #EDEDED;
        font-size: 24px;
        font-family: 'Instrument Sans', sans-serif;
        font-weight: 700;
    }
    
    .add-btn-icon {
        width: 35px;
        height: 35px;
        background: white;
        border: 2px solid #764084;
        border-radius: 50%;
        color: #764084;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .add-btn-icon:hover {
        background: #764084;
        color: white;
        transform: scale(1.1);
    }
    
    /* ===== TIMER DISPLAY ===== */
    .timer-display {
        position: fixed;
        top: 150px;
        right: 20px;
        background: rgba(118, 64, 132, 0.95);
        padding: 1rem 1.5rem;
        border-radius: 15px;
        font-family: 'Instrument Sans', sans-serif;
        font-weight: 700;
        font-size: 18px;
        backdrop-filter: blur(15px);
        z-index: 1000;
        color: white;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* ===== OCULTAR BOTONES INVISIBLES ===== */
    .invisible-btn {
        opacity: 0;
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        z-index: 10;
        cursor: pointer;
    }
    
    /* ===== MEDIA QUERIES RESPONSIVE ===== */
    @media (max-width: 1200px) {
        .content-layout {
            flex-direction: column;
            gap: 2rem;
        }
        
        .learning-list-sidebar {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
        }
        
        .items-grid {
            grid-template-columns: 1fr;
            max-width: 600px;
        }
        
        .navbar-full {
            padding: 0 2%;
        }
    }
    
    @media (max-width: 768px) {
        .navbar-full {
            height: 100px;
            padding: 0 1rem;
        }
        
        .main-container {
            margin-top: 100px;
        }
        
        .navbar-title {
            font-size: 20px;
        }
        
        .spotify-icon {
            transform: scale(0.8);
        }
        
        .main-title {
            font-size: 32px;
            margin: 1.5rem 0;
        }
        
        .main-container {
            padding: 1rem 2%;
        }
        
        .stTextInput > div > div > input {
            font-size: 18px !important;
            padding: 20px 60px 20px 20px !important;
            height: 80px !important;
        }
        
        .action-buttons {
            flex-direction: column;
            align-items: center;
            gap: 1rem;
        }
        
        .action-btn-styled {
            width: 200px !important;
        }
        
        .timer-options {
            flex-direction: column;
            align-items: center;
        }
        
        .item-text {
            font-size: 20px;
        }
        
        .item-card {
            padding: 0 1rem 0 2rem;
            height: 70px;
        }
        
        .learning-list-sidebar {
            padding: 1.5rem;
        }
    }
    
    @media (max-width: 480px) {
        .navbar-title {
            font-size: 18px;
        }
        
        .main-title {
            font-size: 28px;
        }
        
        .items-grid {
            gap: 1rem;
        }
        
        .content-layout {
            gap: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# FUNCIONES AUXILIARES MEJORADAS
# ============================================================================

def add_item_to_learning_list(item_name):
    """Agrega un item a la lista de aprendizaje"""
    if item_name not in st.session_state.learning_list:
        st.session_state.learning_list.append(item_name)
        st.success(f"✅ {item_name} agregado a tu lista de aprendizaje")
        time.sleep(1)  # Breve pausa para mostrar el mensaje
        st.rerun()
    else:
        st.warning(f"⚠️ {item_name} ya está en tu lista")

def remove_item_from_learning_list(item_name):
    """Remueve un item de la lista de aprendizaje"""
    if item_name in st.session_state.learning_list:
        st.session_state.learning_list.remove(item_name)
        st.rerun()

def start_timer_with_minutes(minutes):
    """Inicia el timer con minutos específicos"""
    if minutes and minutes.isdigit() and int(minutes) > 0:
        duration = int(minutes) * 60
        st.session_state.timer_running = True
        st.session_state.timer_start = time.time()
        st.session_state.timer_duration = duration
        st.session_state.timer_minutes = minutes
        st.success(f"⏰ Timer iniciado por {minutes} minutos")
        st.rerun()
    else:
        st.error("⚠️ Por favor ingresa un número válido de minutos")

def start_timer(duration):
    """Inicia el timer con duración específica"""
    st.session_state.timer_running = True
    st.session_state.timer_start = time.time()
    st.session_state.timer_duration = duration
    st.session_state.show_timer_options = False
    st.rerun()

# ============================================================================
# NAVBAR FIJO ARRIBA
# ============================================================================

st.markdown("""
<div class="navbar-full">
    <div class="navbar-left">
        <div class="navbar-title">Spotify for learning</div>
        <div class="spotify-icon">
            <div class="spotify-circle"></div>
            <div class="spotify-overlay"></div>
        </div>
    </div>
    <div class="menu-dots" onclick="toggleMenu()">
        <i class="fas fa-ellipsis-h"></i>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# CONTENIDO PRINCIPAL
# ============================================================================

st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Título principal
st.markdown('<h1 class="main-title">¿Qué aprenderemos hoy?</h1>', unsafe_allow_html=True)

# ============================================================================
# BÚSQUEDA CON TIMER INTEGRADO
# ============================================================================

st.markdown('<div class="search-container">', unsafe_allow_html=True)

# Container del input con timer integrado
st.markdown('<div class="search-input-wrapper">', unsafe_allow_html=True)

# Input principal de búsqueda
search_query = st.text_input(
    "", 
    placeholder="Escribe lo que quieras", 
    key="search_input"
)

# Timer integrado con JavaScript para posicionamiento
st.markdown(f"""
<div class="clock-icon-container">
    <input type="text" class="timer-input" placeholder="min" id="timer-input" value="{st.session_state.get('timer_minutes', '')}">
    <div class="clock-icon" onclick="toggleTimerOptions()">
        <i class="fas fa-clock"></i>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Timer options eliminadas - ahora integradas en el input principal

# ============================================================================
# BOTONES DE ACCIÓN CON ICONOS FONT AWESOME
# ============================================================================

st.markdown('<div class="action-buttons">', unsafe_allow_html=True)

action_col1, action_col2, action_col3 = st.columns([1, 1, 1])

with action_col1:
    if STYLABLE_AVAILABLE:
        with stylable_container(
            key="audio_action_btn",
            css_styles="""
            button {
                background: #764084 !important;
                color: white !important;
                border: none !important;
                border-radius: 40px !important;
                height: 66px !important;
                font-size: 18px !important;
                font-family: 'DM Sans', sans-serif !important;
                font-weight: 700 !important;
                transition: all 0.3s ease !important;
                display: flex !important;
                align-items: center !important;
                gap: 0.5rem !important;
            }
            button:hover {
                background: #8a4d96 !important;
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 25px rgba(118, 64, 132, 0.4) !important;
            }
            """
        ):
            if st.button("🎵 Audio", key="audio_btn", use_container_width=True):
                st.success("🎵 Modo Audio activado")

with action_col2:
    if STYLABLE_AVAILABLE:
        with stylable_container(
            key="resumen_action_btn",
            css_styles="""
            button {
                background: #764084 !important;
                color: white !important;
                border: none !important;
                border-radius: 40px !important;
                height: 66px !important;
                font-size: 18px !important;
                font-family: 'DM Sans', sans-serif !important;
                font-weight: 700 !important;
                transition: all 0.3s ease !important;
                display: flex !important;
                align-items: center !important;
                gap: 0.5rem !important;
            }
            button:hover {
                background: #8a4d96 !important;
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 25px rgba(118, 64, 132, 0.4) !important;
            }
            """
        ):
            if st.button("📝 Resumen", key="resumen_btn", use_container_width=True):
                st.success("📝 Modo Resumen activado")

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# LAYOUT PRINCIPAL: LISTA Y ITEMS
# ============================================================================

st.markdown('<div class="content-layout">', unsafe_allow_html=True)

# ============================================================================
# LISTA DE APRENDIZAJE
# ============================================================================

list_col, items_col = st.columns([1, 2])

with list_col:
    st.markdown("""
    <div class="learning-list-sidebar">
        <div class="learning-list-title">Mi lista de aprendizaje</div>
    """, unsafe_allow_html=True)
    
    if st.session_state.learning_list:
        for item in st.session_state.learning_list:
            item_container = st.container()
            with item_container:
                item_text_col, remove_col = st.columns([4, 1])
                
                with item_text_col:
                    st.markdown(f"""
                    <div class="learning-item-card">
                        <span>{item}</span>
                    </div>
                    """, unsafe_allow_html=True)
                
                with remove_col:
                    if st.button("🗑️", key=f"remove_{item}", help=f"Eliminar {item}"):
                        remove_item_from_learning_list(item)
    else:
        st.markdown('<div class="empty-list-message">Haz clic en + para agregar items aquí</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# GRID DE ITEMS - BOTONES + FUNCIONALES
# ============================================================================

with items_col:
    st.markdown('<div class="items-content">', unsafe_allow_html=True)
    st.markdown('<div class="recommendations-title">Te podría interesar aprender sobre......</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="items-grid">', unsafe_allow_html=True)
    
    items = ["Matemáticas básicas", "Historia del arte", "Programación Python", "Cocina italiana", "Fotografía digital", "Astronomía"]
    
    # Crear grid usando containers
    for i in range(0, len(items), 2):
        row_col1, row_col2 = st.columns(2)
        
        # Primer item de la fila
        with row_col1:
            if i < len(items):
                # Usar container y crear interacción más natural
                with st.container():
                    # Crear un key único para cada item
                    item_key = f"item_card_{i}"
                    
                    # Crear columnas para el texto y el botón
                    text_col, btn_col = st.columns([4, 1])
                    
                    with text_col:
                        st.markdown(f"""
                        <div class="item-card" style="margin-bottom: 10px;">
                            <div class="item-text">{items[i]}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with btn_col:
                        if st.button("➕", key=f"add_{i}", help=f"Agregar {items[i]} a tu lista"):
                            add_item_to_learning_list(items[i])
        
        # Segundo item de la fila
        with row_col2:
            if i+1 < len(items):
                # Usar container y crear interacción más natural
                with st.container():
                    # Crear un key único para cada item
                    item_key = f"item_card_{i+1}"
                    
                    # Crear columnas para el texto y el botón
                    text_col, btn_col = st.columns([4, 1])
                    
                    with text_col:
                        st.markdown(f"""
                        <div class="item-card" style="margin-bottom: 10px;">
                            <div class="item-text">{items[i+1]}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with btn_col:
                        if st.button("➕", key=f"add_{i+1}", help=f"Agregar {items[i+1]} a tu lista"):
                            add_item_to_learning_list(items[i+1])
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# TIMER DISPLAY CON ICONOS
# ============================================================================

if st.session_state.timer_running:
    elapsed = time.time() - st.session_state.timer_start
    remaining = max(0, st.session_state.timer_duration - elapsed)
    
    if remaining > 0:
        minutes = int(remaining // 60)
        seconds = int(remaining % 60)
        st.markdown(f"""
        <div class="timer-display">
            <i class="fas fa-clock"></i>
            <span>{minutes:02d}:{seconds:02d}</span>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1)
        st.rerun()
    else:
        st.session_state.timer_running = False
        st.success("⏰ ¡Tiempo terminado!")
        st.balloons()

# ============================================================================
# JAVASCRIPT PARA INTERACTIVIDAD MEJORADA
# ============================================================================

st.markdown("""
<script>
function toggleMenu() {
    const menuDots = document.querySelector('.menu-dots');
    menuDots.classList.toggle('active');
}

function toggleTimerOptions() {
    const timerInput = document.getElementById('timer-input');
    const minutes = timerInput.value;
    
    if (minutes && parseInt(minutes) > 0) {
        // Simular click en un botón de Streamlit para iniciar timer
        alert(`Timer iniciado por ${minutes} minutos`);
        // En una implementación real, esto triggeraría el timer en Streamlit
    } else {
        // Mostrar opciones rápidas
        const quickOptions = ['5', '10', '15', '25', '45'];
        const choice = prompt('Selecciona minutos: ' + quickOptions.join(', '));
        if (choice && quickOptions.includes(choice)) {
            timerInput.value = choice;
            alert(`Timer iniciado por ${choice} minutos`);
        }
    }
}

// Función para manejar drag and drop (inspirada en el código JS proporcionado)
function initDragAndDrop() {
    const items = document.querySelectorAll('.learning-item-card');
    const holdArea = document.querySelector('.learning-list-sidebar');
    
    items.forEach(item => {
        item.addEventListener('dragstart', function(e) {
            e.dataTransfer.setData('text/plain', '');
            this.style.opacity = '0.5';
        });
        
        item.addEventListener('dragend', function(e) {
            this.style.opacity = '1';
        });
        
        item.setAttribute('draggable', true);
    });
}

// Inicializar funcionalidades cuando la página carga
document.addEventListener('DOMContentLoaded', function() {
    initDragAndDrop();
    
    // Hacer que el input del timer sea más interactivo
    const timerInput = document.getElementById('timer-input');
    if (timerInput) {
        timerInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                toggleTimerOptions();
            }
        });
    }
});
</script>
""", unsafe_allow_html=True)
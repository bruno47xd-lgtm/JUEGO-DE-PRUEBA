import streamlit as st
import random

st.set_page_config(
    page_title="Minecraft Trivia",
    page_icon="💎",
    layout="centered",
)

# -----------------------------
# Estilos temáticos de Minecraft
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background:
            linear-gradient(rgba(12, 25, 18, .88), rgba(12, 25, 18, .94)),
            repeating-linear-gradient(
                0deg,
                #263d28 0px,
                #263d28 18px,
                #304b31 18px,
                #304b31 36px
            );
        color: #f4f4f4;
    }

    .minecraft-title {
        text-align: center;
        font-family: monospace;
        font-size: 42px;
        font-weight: 900;
        color: #7CFC00;
        text-shadow: 4px 4px 0 #173b17;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        font-family: monospace;
        color: #e6e6e6;
        margin-top: 0;
    }

    .question-card {
        background: rgba(20, 20, 20, .82);
        border: 3px solid #5b8c45;
        border-radius: 8px;
        padding: 18px;
        margin: 12px 0;
    }

    .result-card {
        text-align: center;
        background: rgba(0, 0, 0, .82);
        border: 4px solid #c9a227;
        border-radius: 8px;
        padding: 24px;
        font-family: monospace;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 4px;
        border: 2px solid #303030;
        background: #5b8c45;
        color: white;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

QUESTIONS = {
    "BÁSICO": [
        {
            "q": "¿Cuál es el objetivo principal del modo Supervivencia?",
            "options": [
                "Sobrevivir, conseguir recursos y progresar",
                "Construir únicamente casas",
                "Derrotar a todos los aldeanos",
                "Encontrar cinco templos",
                "Conseguir una corona"
            ],
            "answer": 0,
        },
        {
            "q": "¿Qué criatura explota cuando se acerca al jugador?",
            "options": ["Zombi", "Creeper", "Esqueleto", "Araña", "Enderman"],
            "answer": 1,
        },
        {
            "q": "¿Qué herramienta se utiliza normalmente para picar piedra?",
            "options": ["Pala", "Azada", "Hacha", "Pico", "Tijeras"],
            "answer": 3,
        },
        {
            "q": "¿Qué material se necesita para fabricar una mesa de trabajo?",
            "options": [
                "Cuatro tablones de madera",
                "Dos diamantes",
                "Ocho lingotes de hierro",
                "Un bloque de obsidiana",
                "Tres piedras"
            ],
            "answer": 0,
        },
        {
            "q": "¿Cuál de estos animales puede proporcionar lana?",
            "options": ["Vaca", "Cerdo", "Oveja", "Gallina", "Calamar"],
            "answer": 2,
        },
    ],
    "INTERMEDIO": [
        {
            "q": "¿Qué objeto se usa para activar un portal al Nether?",
            "options": ["Pedernal y acero", "Cubo de agua", "Brújula", "Palo", "Reloj"],
            "answer": 0,
        },
        {
            "q": "¿Qué mineral se utiliza para fabricar herramientas de diamante?",
            "options": ["Carbón", "Redstone", "Diamante", "Cuarzo", "Lapislázuli"],
            "answer": 2,
        },
        {
            "q": "¿Qué criatura suele aparecer en el Nether y lanza bolas de fuego?",
            "options": ["Blaze", "Vaca", "Slime", "Zorro", "Guardián"],
            "answer": 0,
        },
        {
            "q": "¿Para qué sirve la redstone principalmente?",
            "options": [
                "Crear mecanismos y circuitos",
                "Cocinar alimentos",
                "Domar caballos",
                "Fabricar lana",
                "Cambiar el clima manualmente"
            ],
            "answer": 0,
        },
        {
            "q": "¿Qué objeto permite respirar bajo el agua durante más tiempo?",
            "options": ["Casco con Afinidad Acuática", "Antorcha", "Cama", "Escudo", "Brújula"],
            "answer": 0,
        },
    ],
    "EXPERTO": [
        {
            "q": "¿Qué estructura se encuentra normalmente en el End y contiene el portal de salida?",
            "options": ["Fortaleza", "Ciudad antigua", "Isla del End", "Templo del desierto", "Mansión"],
            "answer": 2,
        },
        {
            "q": "¿Qué efecto permite al jugador ver claramente bajo el agua?",
            "options": ["Prisa", "Visión nocturna", "Fuerza", "Resistencia", "Salto"],
            "answer": 1,
        },
        {
            "q": "¿Qué bloque se utiliza para crear un faro?",
            "options": ["Vidrio", "Obsidiana", "Netherita", "Esmeralda", "Cristal y estrella del Nether"],
            "answer": 4,
        },
        {
            "q": "¿Qué objeto deja caer el Wither al ser derrotado?",
            "options": ["Perla de Ender", "Estrella del Nether", "Huevo de dragón", "Corazón del mar", "Caña de azúcar"],
            "answer": 1,
        },
        {
            "q": "¿Qué encantamiento permite reparar objetos usando experiencia?",
            "options": ["Fortuna", "Toque de seda", "Irrompibilidad", "Reparación", "Filo"],
            "answer": 3,
        },
    ],
    "VETERANO": [
        {
            "q": "¿Qué combinación permite fabricar una manzana dorada encantada en versiones clásicas?",
            "options": [
                "Manzana y ocho bloques de oro",
                "Manzana y ocho lingotes de hierro",
                "Manzana y ocho diamantes",
                "Pan y oro",
                "Zanahoria y oro"
            ],
            "answer": 0,
        },
        {
            "q": "¿Qué bloque puede mover un pistón, pero no puede ser empujado normalmente por uno pegajoso?",
            "options": ["Piedra", "Obsidiana", "Arena", "Madera", "Tierra"],
            "answer": 1,
        },
        {
            "q": "¿Qué criatura puede aparecer al lanzar un huevo de invocación de aldeano zombi bebé? ",
            "options": ["Aldeano zombi bebé", "Warden", "Ghast", "Shulker", "Ravager"],
            "answer": 0,
        },
        {
            "q": "¿Qué objeto es necesario para localizar una fortaleza del Nether de forma indirecta mediante exploración?",
            "options": ["Ojo de Ender", "Mapa del tesoro", "Brújula", "Reloj", "Catalejo"],
            "answer": 0,
        },
        {
            "q": "¿Qué recurso se necesita para fabricar un bloque de netherita?",
            "options": [
                "Cuatro fragmentos de netherita y cuatro lingotes de oro",
                "Nueve diamantes",
                "Ocho esmeraldas",
                "Un lingote de hierro y carbón",
                "Cuatro cuarzos"
            ],
            "answer": 0,
        },
    ],
}

LEVELS = list(QUESTIONS.keys())

if "started" not in st.session_state:
    st.session_state.started = False
if "level_index" not in st.session_state:
    st.session_state.level_index = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "finished" not in st.session_state:
    st.session_state.finished = False

def reset_game():
    st.session_state.started = False
    st.session_state.level_index = 0
    st.session_state.answers = {}
    st.session_state.submitted = False
    st.session_state.finished = False

st.markdown('<h1 class="minecraft-title">⛏️ MINECRAFT TRIVIA ⛏️</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Cultura general del mundo de Minecraft</p>', unsafe_allow_html=True)

if not st.session_state.started:
    st.info("Responde 20 preguntas repartidas en 4 niveles. Cada pregunta tiene 5 opciones.")
    st.markdown("### Niveles")
    st.write("🟩 BÁSICO · 🟨 INTERMEDIO · 🟥 EXPERTO · 🟪 VETERANO")
    if st.button("▶️ COMENZAR TRIVIA"):
        st.session_state.started = True
        st.rerun()
    st.stop()

if st.session_state.finished:
    total_correct = sum(
        1 for key, value in st.session_state.answers.items()
        if value == QUESTIONS[key[0]][key[1]]["answer"]
    )

    if total_correct == 20:
        emoji = "💎💎💎"
        message = "FELICIDADES, ACERTASTE TODAS"
        detail = "¡Has demostrado dominio absoluto del universo de Minecraft!"
    elif total_correct >= 8:
        emoji = "🪙⛓️"
        message = "BUEN TRABAJO"
        detail = "Has conseguido una buena cantidad de recursos."
    elif total_correct > 0:
        emoji = "🪨"
        message = "BUEN INTENTO"
        detail = "Sigue explorando, minando y aprendiendo."
    else:
        emoji = "💣"
        message = "HAS PERDIDO"
        detail = "El TNT explotó… ¡inténtalo de nuevo!"

    st.markdown(
        f"""
        <div class="result-card">
            <div style="font-size:64px;">{emoji}</div>
            <h2>{message}</h2>
            <p>{detail}</p>
            <h3>Puntuación: {total_correct} / 20</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.balloons() if total_correct == 20 else None

    if st.button("🔁 JUGAR DE NUEVO"):
        reset_game()
        st.rerun()
    st.stop()

level_name = LEVELS[st.session_state.level_index]
questions = QUESTIONS[level_name]

st.progress(st.session_state.level_index / len(LEVELS))
st.subheader(f"Nivel {st.session_state.level_index + 1} de 4: {level_name}")
st.caption("Selecciona una respuesta para cada pregunta y pulsa el botón del nivel.")

with st.form(f"form_{level_name}"):
    for i, question in enumerate(questions):
        st.markdown(
            f'<div class="question-card"><strong>{i + 1}. {question["q"]}</strong></div>',
            unsafe_allow_html=True,
        )
        selected = st.radio(
            "Elige una opción:",
            question["options"],
            key=f"{level_name}_{i}",
            index=None,
        )
        if selected is not None:
            st.session_state.answers[(level_name, i)] = question["options"].index(selected)

    submitted = st.form_submit_button(
        "✅ GUARDAR NIVEL Y CONTINUAR"
        if st.session_state.level_index < 3
        else "🏁 TERMINAR TRIVIA"
    )

if submitted:
    if st.session_state.level_index < 3:
        st.session_state.level_index += 1
        st.rerun()
    else:
        st.session_state.finished = True
        st.rerun()

from pathlib import Path
import zipfile, textwrap

base = Path("/mnt/data/minecraft_trivia_streamlit")
base.mkdir(exist_ok=True)

app_py = r'''
import streamlit as st

st.set_page_config(
    page_title="Minecraft Trivia",
    page_icon="⛏️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# ESTILOS
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Roboto:wght@400;700;900&display=swap');

.stApp {
    background:
        linear-gradient(rgba(0,0,0,.18), rgba(0,0,0,.35)),
        linear-gradient(180deg, #75c9ff 0%, #b9e8ff 35%, #77b852 35%, #5b9b3c 100%);
    background-attachment: fixed;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.mc-title {
    font-family: 'Press Start 2P', monospace;
    text-align: center;
    color: #ffffff;
    text-shadow: 4px 4px 0 #2d2d2d;
    font-size: clamp(1.6rem, 5vw, 3rem);
    line-height: 1.35;
    margin-bottom: .5rem;
}

.mc-subtitle {
    text-align: center;
    font-weight: 900;
    color: #17340d;
    font-size: 1.15rem;
    margin-bottom: 1.5rem;
}

.level-card {
    background: rgba(32, 32, 32, .90);
    border: 4px solid #111;
    box-shadow: 7px 7px 0 rgba(0,0,0,.45);
    padding: 1.25rem;
    color: white;
    margin-bottom: 1rem;
}

.question-card {
    background: rgba(255,255,255,.96);
    border: 4px solid #3f3f3f;
    box-shadow: 6px 6px 0 rgba(0,0,0,.35);
    padding: 1.2rem;
    margin: 1rem 0;
    border-radius: 2px;
}

.question-number {
    color: #3f3f3f;
    font-weight: 900;
    font-size: .95rem;
}

.question-text {
    color: #111;
    font-size: 1.15rem;
    font-weight: 900;
    margin-top: .45rem;
}

.result-box {
    background: rgba(25,25,25,.94);
    border: 5px solid #111;
    box-shadow: 9px 9px 0 rgba(0,0,0,.45);
    padding: 2rem 1rem;
    text-align: center;
    color: white;
    margin-top: 1rem;
}

.result-title {
    font-family: 'Press Start 2P', monospace;
    font-size: clamp(1.2rem, 4vw, 2rem);
    line-height: 1.5;
    color: #fff;
    text-shadow: 3px 3px 0 #000;
}

.result-score {
    font-size: 1.4rem;
    font-weight: 900;
    margin: 1rem 0;
}

.pixel {
    font-size: 4rem;
    letter-spacing: .25rem;
    line-height: 1.4;
}

.small-note {
    text-align: center;
    color: #17340d;
    font-weight: 700;
    margin-top: 1rem;
}

div.stButton > button {
    width: 100%;
    background: #5e5e5e;
    color: white;
    border: 3px solid #202020;
    border-radius: 2px;
    box-shadow: 4px 4px 0 #202020;
    font-weight: 900;
    min-height: 3rem;
}

div.stButton > button:hover {
    background: #777;
    color: white;
    border-color: #111;
}

[data-testid="stRadio"] label {
    font-weight: 700;
}

hr {
    border-top: 3px solid rgba(0,0,0,.25);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# PREGUNTAS
# -----------------------------
QUESTIONS = [
    {
        "level": "BÁSICO",
        "questions": [
            ("¿Qué criatura explota cuando se acerca al jugador?", ["Creeper", "Esqueleto", "Zombi", "Araña", "Enderman"], 0),
            ("¿Qué material se necesita para fabricar una mesa de crafteo?", ["Madera", "Piedra", "Hierro", "Diamante", "Oro"], 0),
            ("¿Cuál de estos es un mineral que puede encontrarse bajo tierra?", ["Diamante", "Arena", "Lana", "Arcilla", "Hojas"], 0),
            ("¿Qué herramienta se utiliza principalmente para picar piedra?", ["Pico", "Hacha", "Pala", "Azada", "Tijeras"], 0),
            ("¿Qué dimensión tiene un portal hecho con obsidiana?", ["Nether", "End", "Aether", "Overworld 2", "Deep Dark"], 0),
        ],
    },
    {
        "level": "INTERMEDIO",
        "questions": [
            ("¿Qué objeto se utiliza para activar un portal al Nether?", ["Pedernal y acero", "Cubo de agua", "Antorcha", "Polvo de redstone", "Caña de pescar"], 0),
            ("¿Qué criatura puede aparecer al usar un huevo de dragón? ", ["Ninguna criatura", "Dragón bebé", "Enderman", "Ghast", "Warden"], 0),
            ("¿Cuál es el nombre del jefe que aparece en el End?", ["Dragón del End", "Wither", "Warden", "Elder Guardian", "Ravager"], 0),
            ("¿Qué alimento puede curar a un lobo domesticado?", ["Carne", "Pan", "Poción de curación", "Zanahoria dorada", "Galleta"], 0),
            ("¿Qué bloque permite convertir aldeanos y comerciar con ellos según su profesión?", ["Bloques de trabajo", "Cofres", "Hornos", "Yunques", "Observadores"], 0),
        ],
    },
    {
        "level": "EXPERTO",
        "questions": [
            ("¿Qué encantamiento permite reparar objetos usando experiencia?", ["Reparación (Mending)", "Fortuna", "Toque de seda", "Filo", "Eficiencia"], 0),
            ("¿Qué estructura contiene normalmente un generador de monstruos (spawner) de mazmorra?", ["Mazmorra", "Aldea", "Templo del desierto", "Mansión", "Fortaleza del Nether"], 0),
            ("¿Qué ingrediente se necesita para fabricar una poción de visión nocturna?", ["Zanahoria dorada", "Manzana dorada", "Ojo de araña", "Pez globo", "Melón brillante"], 0),
            ("¿Qué bloque emite una señal de redstone cuando detecta cambios en su entorno?", ["Observador", "Pistón", "Dispensador", "Tolva", "Comparador"], 0),
            ("¿Cuál de estos efectos puede obtenerse al comer un estofado sospechoso, dependiendo del ingrediente?", ["Un efecto de estado", "Más vida permanente", "Vuelo", "Invisibilidad permanente", "Regeneración infinita"], 0),
        ],
    },
    {
        "level": "VETERANO",
        "questions": [
            ("¿Cuál es el nombre de la dimensión en la que aparece el Dragón del End?", ["El End", "El Nether", "El Vacío", "El Deep Dark", "El Overworld"], 0),
            ("¿Qué recurso es necesario para fabricar un faro (beacon)?", ["Estrella del Nether", "Perla de Ender", "Fragmento de amatista", "Corazón del mar", "Membrana de fantasma"], 0),
            ("¿Qué criatura deja caer membranas de fantasma?", ["Fantasma", "Ghast", "Phantom", "Shulker", "Vex"], 0),
            ("¿Qué objeto permite localizar fortalezas del Nether?", ["No existe un objeto que las localice directamente", "Ojo de Ender", "Brújula", "Mapa del tesoro", "Reloj"], 0),
            ("¿Qué bloque puede almacenar experiencia y se encuentra en ciudades antiguas?", ["No hay un bloque que almacene experiencia allí de forma exclusiva", "Cofre de sculk", "Catalizador", "Sensor de sculk", "Calibrated Sculk Sensor"], 0),
        ],
    },
]

# Correcciones para algunas preguntas: se mantienen 5 opciones y se marca la correcta.
# Índices correctos:
# BÁSICO: 0,0,0,0,0
# INTERMEDIO: 0,0,0,0,0
# EXPERTO: 0,0,0,0,0
# VETERANO: 0,0,2,0,0

QUESTIONS[3]["questions"][2] = (
    "¿Qué criatura deja caer membranas de fantasma?",
    ["Ghast", "Warden", "Phantom", "Shulker", "Vex"],
    2,
)

# Pregunta intermedia 2: el huevo de dragón no genera ninguna criatura.
# La redacción se conserva como pregunta de conocimiento.

LEVEL_EMOJIS = {
    "BÁSICO": "🟩",
    "INTERMEDIO": "🟨",
    "EXPERTO": "🟧",
    "VETERANO": "🟥",
}

def reset_quiz():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# -----------------------------
# CABECERA
# -----------------------------
st.markdown('<div class="mc-title">⛏️ MINECRAFT TRIVIA ⛏️</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="mc-subtitle">CULTURA GENERAL DEL JUEGO · 20 PREGUNTAS · 4 NIVELES</div>',
    unsafe_allow_html=True
)

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if not st.session_state.submitted:
    st.markdown("""
    <div class="level-card">
        <b>🎮 ¿ESTÁS PREPARADO?</b><br><br>
        Responde las 20 preguntas. Cada nivel tiene 5 preguntas y cada pregunta tiene 5 opciones.
        Cuando termines, pulsa <b>COMPROBAR RESULTADOS</b>.
    </div>
    """, unsafe_allow_html=True)

    question_counter = 0

    for level_data in QUESTIONS:
        level = level_data["level"]
        st.markdown(
            f'<div class="level-card"><b>{LEVEL_EMOJIS[level]} NIVEL {level}</b></div>',
            unsafe_allow_html=True
        )

        for local_i, (question, options, correct) in enumerate(level_data["questions"]):
            question_counter += 1
            st.markdown(
                f"""
                <div class="question-card">
                    <div class="question-number">PREGUNTA {question_counter}/20</div>
                    <div class="question-text">{question}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.radio(
                "Elige una opción:",
                options,
                key=f"q_{question_counter}",
                index=None,
                label_visibility="collapsed",
            )

    st.divider()

    if st.button("🧪 COMPROBAR RESULTADOS", type="primary", use_container_width=True):
        unanswered = [
            i for i in range(1, 21)
            if st.session_state.get(f"q_{i}") is None
        ]

        if unanswered:
            st.warning(
                f"⚠️ Te faltan {len(unanswered)} pregunta(s) por responder. "
                "Contesta todas antes de comprobar el resultado."
            )
        else:
            score = 0
            qnum = 0
            for level_data in QUESTIONS:
                for question, options, correct in level_data["questions"]:
                    qnum += 1
                    if st.session_state[f"q_{qnum}"] == options[correct]:
                        score += 1

            st.session_state.score = score
            st.session_state.submitted = True
            st.rerun()

    st.markdown(
        '<div class="small-note">💡 Consejo: piensa como un jugador veterano antes de marcar.</div>',
        unsafe_allow_html=True
    )

else:
    score = st.session_state.score

    if score == 20:
        icon = "💎 💎 💎"
        title = "FELICIDADES, ACERTASTE TODAS"
        detail = "¡Has dominado la trivia de Minecraft!"
    elif score >= 10:
        icon = "🥇 🪙 ⛓️ 🪙 🥇"
        title = "BUEN TRABAJO"
        detail = "¡Has conseguido una buena cantidad de conocimientos de Minecraft!"
    elif score > 0:
        icon = "🪨 ⛏️ 🪨"
        title = "BUEN INTENTO"
        detail = "¡Sigue explorando, minando y aprendiendo!"
    else:
        icon = "💥 🧨 💥"
        title = "HAS PERDIDO"
        detail = "El TNT hizo BOOM... ¡pero siempre puedes volver a intentarlo!"

    st.markdown(
        f"""
        <div class="result-box">
            <div class="pixel">{icon}</div>
            <div class="result-title">{title}</div>
            <div class="result-score">PUNTUACIÓN: {score}/20</div>
            <p>{detail}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Celebraciones visuales de Streamlit
    if score == 20:
        st.balloons()
    elif score >= 10:
        st.snow()

    st.markdown("### 📊 Tu resultado por nivel")

    qnum = 0
    level_scores = {}
    for level_data in QUESTIONS:
        level = level_data["level"]
        level_score = 0
        for question, options, correct in level_data["questions"]:
            qnum += 1
            if st.session_state.get(f"q_{qnum}") == options[correct]:
                level_score += 1
        level_scores[level] = level_score

    for level, level_score in level_scores.items():
        st.progress(level_score / 5, text=f"{level}: {level_score}/5")

    st.divider()

    if st.button("🔄 JUGAR DE NUEVO", use_container_width=True):
        reset_quiz()

st.markdown(
    '<div class="small-note">Hecho con ❤️, Streamlit y espíritu de Minecraft · gptonline.ai</div>',
    unsafe_allow_html=True
)
'''

requirements = """streamlit>=1.40,<2
"""

readme = r'''# ⛏️ Minecraft Trivia — Streamlit

Trivia de cultura general sobre Minecraft con:

- 4 niveles: BÁSICO, INTERMEDIO, EXPERTO y VETERANO.
- 5 preguntas por nivel.
- 20 preguntas en total.
- 5 opciones por pregunta.
- Resultado final según puntuación:
  - 💎 20/20 → **FELICIDADES, ACERTASTE TODAS**
  - 🥇 10–19 → **BUEN TRABAJO**
  - 🪨 1–9 → **BUEN INTENTO**
  - 💥 0 → **HAS PERDIDO**
- Diseño inspirado en una estética pixel/Minecraft.
- Desglose de puntuación por nivel.
- Botón para volver a jugar.

## Ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run app.py

import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Trivia de Minecraft", page_icon="⛏️", layout="centered")

# Estilos CSS personalizados para darle un toque temático
st.markdown("""
    <style>
    .titulo { text-align: center; color: #4CAF50; font-family: 'Courier New', monospace; font-size: 40px; font-weight: bold;}
    .nivel { color: #FF9800; border-bottom: 2px solid #FF9800; padding-bottom: 5px; }
    .stRadio > label { font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='titulo'>⛏️ TRIVIA CULTURA GENERAL DE MINECRAFT ⛏️</div>", unsafe_allow_html=True)
st.write("¡Demuestra tus conocimientos sobre Minecraft! Responde estas 20 preguntas divididas en 4 niveles de dificultad.")

# Base de datos de preguntas
preguntas = {
    "BÁSICO": [
        {"q": "1. ¿Cuál es el material más básico para empezar a crear herramientas?", "options": ["Tierra", "Piedra", "Madera", "Hierro", "Diamante"], "ans": "Madera"},
        {"q": "2. ¿Qué criatura (mob) verde explota cuando se acerca al jugador?", "options": ["Zombi", "Esqueleto", "Creeper", "Enderman", "Araña"], "ans": "Creeper"},
        {"q": "3. ¿Qué herramienta es la correcta y más rápida para picar piedra?", "options": ["Hacha", "Pala", "Espada", "Pico", "Azada"], "ans": "Pico"},
        {"q": "4. ¿En qué dimensión final se encuentra el Dragón de Ender?", "options": ["El Nether", "El Overworld", "El End", "El Vacío", "Las Cuevas Profundas"], "ans": "El End"},
        {"q": "5. ¿Qué mineral se usa comúnmente para hacer tu primera armadura resistente y escudos?", "options": ["Oro", "Cobre", "Hierro", "Esmeralda", "Lápislázuli"], "ans": "Hierro"}
    ],
    "INTERMEDIO": [
        {"q": "6. ¿Cómo se llama el reino infernal al que se accede con un portal de obsidiana?", "options": ["El Aether", "El Nether", "Tierras Bajas", "El Núcleo", "Dimensión Carmesí"], "ans": "El Nether"},
        {"q": "7. ¿Qué bloque se utiliza para encantar armas y herramientas?", "options": ["Yunque", "Piedra de afilar", "Mesa de trabajo", "Mesa de encantamientos", "Soporte para pociones"], "ans": "Mesa de encantamientos"},
        {"q": "8. ¿Qué criatura neutral y alta se vuelve hostil si la miras directamente a los ojos?", "options": ["Lobo", "Golem de Hierro", "Enderman", "Piglin", "Aldeano"], "ans": "Enderman"},
        {"q": "9. ¿Cuál es el nivel máximo de experiencia requerido para el mejor encanto en una mesa rodeada de librerías?", "options": ["Nivel 15", "Nivel 20", "Nivel 30", "Nivel 50", "Nivel 100"], "ans": "Nivel 30"},
        {"q": "10. ¿Qué objeto necesitas obligatoriamente para recolectar agua o lava?", "options": ["Frasco de cristal", "Cuenco de madera", "Cubo de hierro", "Vaso", "Saco"], "ans": "Cubo de hierro"}
    ],
    "EXPERTO": [
        {"q": "11. ¿Qué bloque no puede ser movido por un pistón normal ni pegajoso?", "options": ["Tierra", "Madera", "Obsidiana", "Cristal", "Arena"], "ans": "Obsidiana"},
        {"q": "12. ¿Qué poción específica necesitas lanzarle a un aldeano zombi para curarlo (junto con una manzana dorada)?", "options": ["Poción de Curación", "Poción de Regeneración", "Poción de Debilidad", "Poción de Fuerza", "Poción de Resistencia al fuego"], "ans": "Poción de Debilidad"},
        {"q": "13. ¿Cuál es la probabilidad base (aprox) de que una oveja nazca de color rosa naturalmente?", "options": ["1.000%", "0.164%", "0.500%", "5.000%", "0.001%"], "ans": "0.164%"},
        {"q": "14. En las versiones recientes (1.18+), ¿en qué coordenada 'Y' es más óptimo encontrar diamantes?", "options": ["Y = 11", "Y = 12", "Y = 0", "Y = -59", "Y = -64"], "ans": "Y = -59"},
        {"q": "15. ¿Qué mob de las Mansiones del Bosque es capaz de invocar Vexes (Ánimas)?", "options": ["Saqueador (Pillager)", "Vindicador", "Invocador (Evoker)", "Bruja", "Ilusionista"], "ans": "Invocador (Evoker)"}
    ],
    "VETERANO": [
        {"q": "16. ¿Cuál es el límite máximo de altura para construir bloques en el Overworld en las versiones actuales?", "options": ["256 bloques", "320 bloques", "512 bloques", "128 bloques", "1024 bloques"], "ans": "320 bloques"},
        {"q": "17. ¿Qué disco de música del juego está visualmente roto y tiene un audio sumamente espeluznante?", "options": ["Disco 13", "Disco 11", "Mellohi", "Stal", "Pigstep"], "ans": "Disco 11"},
        {"q": "18. ¿Cómo se conocía al límite del mapa glitcheado que se generaba a millones de bloques en versiones antiguas (Beta)?", "options": ["El Vacío", "Far Lands (Tierras Lejanas)", "El Muro de Hielo", "El Borde del Mundo", "La Barrera"], "ans": "Far Lands (Tierras Lejanas)"},
        {"q": "19. ¿A cuántos tics (ticks) de redstone equivale exactamente un segundo en la vida real?", "options": ["20 tics", "10 tics", "5 tics", "15 tics", "40 tics"], "ans": "10 tics"},
        {"q": "20. ¿Quién es el creador original de Minecraft, también conocido por su apodo?", "options": ["Jeb (Jens Bergensten)", "Notch (Markus Persson)", "Dinnerbone (Nathan Adams)", "C418 (Daniel Rosenfeld)", "Keralis"], "ans": "Notch (Markus Persson)"}
    ]
}

# Formulario para las preguntas
with st.form("formulario_trivia"):
    respuestas_usuario = {}
    
    for nivel, pregs in preguntas.items():
        st.markdown(f"<h2 class='nivel'>Nivel: {nivel}</h2>", unsafe_allow_html=True)
        for i, p in enumerate(pregs):
            st.markdown(f"**{p['q']}**")
            # Clave única para cada pregunta
            clave = f"{nivel}_{i}"
            respuestas_usuario[clave] = st.radio("Selecciona tu respuesta:", p["options"], key=clave, index=None)
            st.write("---")
            
    boton_enviar = st.form_submit_button("Terminar Trivia y Ver Puntuación")

# Lógica de puntuación
if boton_enviar:
    puntaje = 0
    # Verificamos que haya respondido todas (opcional, pero buena práctica)
    if None in respuestas_usuario.values():
        st.warning("⚠️ Parece que dejaste algunas preguntas sin responder. ¡Intenta marcar todas para obtener tu puntaje real!")
        
    for nivel, pregs in preguntas.items():
        for i, p in enumerate(pregs):
            clave = f"{nivel}_{i}"
            if respuestas_usuario[clave] == p["ans"]:
                puntaje += 1
                
    st.markdown(f"## Tu Puntaje Final: {puntaje} / 20")
    
    # Sistema de premios y mensajes solicitado
    if puntaje == 20:
        st.success("💎💎💎 FELICIDADES, ACERTASTE TODAS 💎💎💎")
        st.balloons()
    elif puntaje >= 10:
        st.info("🥇🥈 BUEN TRABAJO 🥇🥈 (Lingotes de Oro y Hierro)")
    elif puntaje > 0:
        st.warning("⬛⬛ BUEN INTENTO ⬛⬛ (Carbón)")
    else:
        st.error("🧨🧨 HAS PERDIDO 🧨🧨 (TNT)")

import React, { useState, useEffect } from 'react';

const questions = [
  // NIVEL 1: BÁSICO
  {
    level: "Básico",
    question: "¿Cuál es el bloque más común en la superficie del mundo normal (Overworld)?",
    options: ["Piedra", "Tierra", "Madera", "Arena", "Grava"],
    answer: "Tierra"
  },
  {
    level: "Básico",
    question: "¿Qué herramienta es la más rápida para romper piedra?",
    options: ["Hacha", "Pala", "Espada", "Pico", "Azada"],
    answer: "Pico"
  },
  {
    level: "Básico",
    question: "¿Qué criatura explota silenciosamente al acercarse al jugador?",
    options: ["Zombi", "Esqueleto", "Creeper", "Enderman", "Araña"],
    answer: "Creeper"
  },
  {
    level: "Básico",
    question: "¿Con qué material principal se construye un portal al Nether?",
    options: ["Bedrock", "Piedra", "Ladrillos del Nether", "Cuarzo", "Obsidiana"],
    answer: "Obsidiana"
  },
  {
    level: "Básico",
    question: "¿Qué mineral se usa típicamente para crear tu primera armadura duradera?",
    options: ["Oro", "Cobre", "Hierro", "Diamante", "Esmeralda"],
    answer: "Hierro"
  },

  // NIVEL 2: INTERMEDIO
  {
    level: "Intermedio",
    question: "¿Cuántos bloques de hierro se necesitan para construir un Gólem de Hierro?",
    options: ["2", "3", "4", "5", "6"],
    answer: "4"
  },
  {
    level: "Intermedio",
    question: "¿Qué objeto necesitas para domesticar a un lobo?",
    options: ["Carne podrida", "Pescado crudo", "Zanahoria", "Manzana", "Hueso"],
    answer: "Hueso"
  },
  {
    level: "Intermedio",
    question: "¿Cuál es la altura máxima de construcción (Y) en las versiones recientes (1.18+)?",
    options: ["128", "256", "319", "320", "512"],
    answer: "320"
  },
  {
    level: "Intermedio",
    question: "¿Qué objeto deja caer el Enderman al morir?",
    options: ["Ojo de Ender", "Perla de Ender", "Lágrima de Ghast", "Vara de Blaze", "Polvo de Redstone"],
    answer: "Perla de Ender"
  },
  {
    level: "Intermedio",
    question: "¿Cómo se llama el jefe final del juego que reside en el End?",
    options: ["Wither", "Guardián Anciano", "Warden", "Rey Esqueleto", "Dragón del Ender"],
    answer: "Dragón del Ender"
  },

  // NIVEL 3: EXPERTO
  {
    level: "Experto",
    question: "¿En qué coordenada 'Y' es más óptimo minar diamantes en la versión 1.18+?",
    options: ["Y=11", "Y=12", "Y=0", "Y=-59", "Y=-64"],
    answer: "Y=-59"
  },
  {
    level: "Experto",
    question: "¿Cuál era el nombre original de Minecraft durante sus primeros días de desarrollo?",
    options: ["Cave Game", "Block Builder", "Mine and Craft", "Infiniminer", "Voxel World"],
    answer: "Cave Game"
  },
  {
    level: "Experto",
    question: "¿Qué disco de música está visiblemente roto y tiene un sonido aterrador?",
    options: ["Stal", "Pigstep", "11", "13", "Mellohi"],
    answer: "11"
  },
  {
    level: "Experto",
    question: "¿Qué encantamiento congela el agua bajo tus pies al caminar?",
    options: ["Caída de Pluma", "Agilidad Acuática", "Toque de Seda", "Paso Helado", "Empuje"],
    answer: "Paso Helado"
  },
  {
    level: "Experto",
    question: "¿Cuál de estas criaturas NO es clasificada como un no-muerto (undead)?",
    options: ["Zombi", "Esqueleto Wither", "Creeper", "Ahogado", "Caballo Esqueleto"],
    answer: "Creeper"
  },

  // NIVEL 4: VETERANO
  {
    level: "Veterano",
    question: "¿En qué fecha se lanzó oficialmente la versión 1.0 de Minecraft?",
    options: ["17 de Mayo de 2009", "15 de Agosto de 2010", "18 de Noviembre de 2011", "21 de Diciembre de 2011", "10 de Septiembre de 2012"],
    answer: "18 de Noviembre de 2011"
  },
  {
    level: "Veterano",
    question: "¿Quién fue el creador original de Minecraft, también conocido por su alias?",
    options: ["Jeb", "Notch", "Dinnerbone", "C418", "Kens"],
    answer: "Notch"
  },
  {
    level: "Veterano",
    question: "¿Cuánta experiencia (puntos en total) se necesita exactamente para llegar al nivel 30 desde cero?",
    options: ["825", "1395", "1500", "2045", "3000"],
    answer: "1395"
  },
  {
    level: "Veterano",
    question: "¿Cuál es la probabilidad exacta de que una oveja nazca con lana rosa de forma natural?",
    options: ["0.164%", "1.000%", "5.000%", "0.010%", "0.500%"],
    answer: "0.164%"
  },
  {
    level: "Veterano",
    question: "¿Cuántos 'ticks de juego' (game ticks) equivalen a un segundo en Minecraft sin lag?",
    options: ["10", "15", "20", "30", "60"],
    answer: "20"
  }
];

export default function MinecraftTrivia() {
  const [gameState, setGameState] = useState('START'); // START, PLAYING, END
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [selectedOption, setSelectedOption] = useState(null);
  const [isAnswering, setIsAnswering] = useState(false);

  // Inyectar fuente de estilo pixel art al montar
  useEffect(() => {
    const link = document.createElement('link');
    link.href = 'https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap';
    link.rel = 'stylesheet';
    document.head.appendChild(link);
    return () => { document.head.removeChild(link); };
  }, []);

  const styles = {
    font: { fontFamily: "'Press Start 2P', cursive" },
    textShadow: { textShadow: '2px 2px 0px #000' },
    mcButton: {
      backgroundColor: '#c6c6c6',
      border: '4px solid',
      borderTopColor: '#ffffff',
      borderLeftColor: '#ffffff',
      borderBottomColor: '#555555',
      borderRightColor: '#555555',
      boxShadow: 'inset -2px -2px 0px rgba(0,0,0,0.25)',
      color: '#000',
      textShadow: '1px 1px 0px #ddd'
    },
    mcButtonHover: {
      backgroundColor: '#d6d6d6',
    },
    mcPanel: {
      backgroundColor: 'rgba(0, 0, 0, 0.7)',
      border: '4px solid #555'
    }
  };

  const startGame = () => {
    setGameState('PLAYING');
    setCurrentQuestionIndex(0);
    setScore(0);
    setSelectedOption(null);
    setIsAnswering(false);
  };

  const handleAnswer = (option) => {
    if (isAnswering) return;
    
    setSelectedOption(option);
    setIsAnswering(true);

    const currentQuestion = questions[currentQuestionIndex];
    if (option === currentQuestion.answer) {
      setScore(prev => prev + 1);
    }

    // Esperar un poco antes de pasar a la siguiente
    setTimeout(() => {
      if (currentQuestionIndex + 1 < questions.length) {
        setCurrentQuestionIndex(prev => prev + 1);
        setSelectedOption(null);
        setIsAnswering(false);
      } else {
        setGameState('END');
      }
    }, 1200);
  };

  const renderStart = () => (
    <div className="flex flex-col items-center justify-center h-full w-full p-6 text-center z-10" style={styles.font}>
      <div style={styles.mcPanel} className="p-10 rounded shadow-2xl max-w-2xl w-full flex flex-col items-center">
        <h1 className="text-4xl md:text-5xl text-yellow-300 mb-6 leading-tight" style={styles.textShadow}>
          TRIVIA DE MINECRAFT
        </h1>
        <p className="text-white text-sm md:text-base mb-8 leading-relaxed" style={styles.textShadow}>
          Pon a prueba tu conocimiento. <br/>
          4 Niveles, 20 Preguntas. <br/>
          ¿Podrás conseguir el Diamante?
        </p>
        <button 
          onClick={startGame}
          className="w-full md:w-auto px-8 py-4 text-xl hover:bg-gray-100 transition transform hover:scale-105"
          style={styles.mcButton}
        >
          JUGAR
        </button>
      </div>
    </div>
  );

  const renderPlaying = () => {
    const q = questions[currentQuestionIndex];
    const progress = ((currentQuestionIndex) / questions.length) * 100;

    return (
      <div className="flex flex-col items-center w-full h-full p-4 md:p-8 z-10" style={styles.font}>
        
        {/* Header (Score & Progress) */}
        <div className="w-full max-w-3xl flex justify-between items-center mb-6 text-white text-xs md:text-sm">
          <div style={styles.textShadow}>NIVEL: <span className="text-green-400">{q.level}</span></div>
          <div style={styles.textShadow}>PUNTAJE: {score}</div>
        </div>

        {/* Progress bar */}
        <div className="w-full max-w-3xl bg-gray-800 h-4 border-2 border-black mb-8">
          <div className="bg-green-500 h-full transition-all duration-300" style={{width: `${progress}%`}}></div>
        </div>

        {/* Question Panel */}
        <div style={styles.mcPanel} className="p-6 md:p-8 w-full max-w-3xl flex flex-col items-center mb-8">
          <h2 className="text-white text-sm md:text-lg mb-4 text-center text-gray-400">
            Pregunta {currentQuestionIndex + 1} de {questions.length}
          </h2>
          <p className="text-white text-base md:text-xl text-center leading-relaxed mb-6" style={styles.textShadow}>
            {q.question}
          </p>
        </div>

        {/* Options Grid */}
        <div className="w-full max-w-3xl grid grid-cols-1 md:grid-cols-2 gap-4">
          {q.options.map((option, index) => {
            let bgColorClass = "";
            let btnStyles = { ...styles.mcButton };
            
            if (isAnswering) {
              if (option === q.answer) {
                // Respuesta correcta en verde estilo minecraft
                btnStyles.backgroundColor = '#55FF55';
              } else if (option === selectedOption) {
                // Respuesta incorrecta elegida en rojo
                btnStyles.backgroundColor = '#FF5555';
              }
            }

            return (
              <button
                key={index}
                onClick={() => handleAnswer(option)}
                disabled={isAnswering}
                className={`px-4 py-4 text-xs md:text-sm transition-transform active:scale-95 text-center ${index === 4 ? "md:col-span-2" : ""}`}
                style={btnStyles}
              >
                {option}
              </button>
            );
          })}
        </div>
      </div>
    );
  };

  const renderEnd = () => {
    let resultMessage = "";
    let emojis = "";
    
    if (score === 20) {
      emojis = "💎💎💎";
      resultMessage = "FELICIDADES, ACERTASTE TODAS";
    } else if (score >= 10 && score <= 19) {
      emojis = "🥇🪙🛡️";
      resultMessage = "BUEN TRABAJO";
    } else if (score >= 1 && score <= 9) {
      emojis = "⬛🪨";
      resultMessage = "BUEN INTENTO";
    } else {
      emojis = "🧨";
      resultMessage = "HAS PERDIDO";
    }

    return (
      <div className="flex flex-col items-center justify-center h-full w-full p-6 text-center z-10" style={styles.font}>
        <div style={styles.mcPanel} className="p-10 rounded shadow-2xl max-w-2xl w-full flex flex-col items-center">
          
          <div className="text-6xl mb-6">{emojis}</div>
          
          <h1 className="text-2xl md:text-3xl text-yellow-300 mb-6 leading-tight" style={styles.textShadow}>
            {resultMessage}
          </h1>
          
          <p className="text-white text-lg md:text-xl mb-10" style={styles.textShadow}>
            Puntaje Final: {score} / {questions.length}
          </p>

          <button 
            onClick={startGame}
            className="w-full md:w-auto px-8 py-4 text-sm md:text-base transition transform hover:scale-105"
            style={styles.mcButton}
          >
            VOLVER A JUGAR
          </button>
        </div>
      </div>
    );
  };

  return (
    // Fondo general que simula bloque de tierra
    <div className="min-h-screen flex flex-col relative bg-green-900" 
         style={{
           backgroundImage: 'repeating-linear-gradient(45deg, #5b3e2b 25%, transparent 25%, transparent 75%, #5b3e2b 75%, #5b3e2b), repeating-linear-gradient(45deg, #5b3e2b 25%, #4a3222 25%, #4a3222 75%, #5b3e2b 75%, #5b3e2b)',
           backgroundPosition: '0 0, 20px 20px',
           backgroundSize: '40px 40px'
         }}>
      
      {/* Capa de oscurecimiento (para dar contraste) */}
      <div className="absolute inset-0 bg-black bg-opacity-40 z-0"></div>

      <main className="flex-grow flex items-center justify-center overflow-y-auto">
        {gameState === 'START' && renderStart()}
        {gameState === 'PLAYING' && renderPlaying()}
        {gameState === 'END' && renderEnd()}
      </main>
    </div>
  );
}

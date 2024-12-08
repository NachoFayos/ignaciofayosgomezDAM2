var desfase_global_x = 0;                         // Desfase global para el lienzo (desplazamiento del lienzo)
const anchoNivel = 2048;                          // Ancho del nivel 
let victoriaMostrada = false;                     // Variable para controlar si ya se mostró el mensaje de victoria
let mensajeActivo = false;                        // Variable para indicar si el mensaje está en pantalla

if (typeof misnpcs === "undefined") {             // Asegurarse de que misnpcs existe y está inicializado, solo se inicia sino está definido
    var misnpcs = [];                             // Solo inicializa si no está definido
}

const cantidadNPCs = 20;                          // Número total de NPCs
    if (misnpcs.length === 0) {
        for (let i = 0; i < cantidadNPCs; i++) {
        misnpcs.push(new Npc());
        }
    }

function bucle() {
    actualizarMovimientoJugador();                                                  // Se actualizar movimiento del jugador
    contexto.clearRect(0, 0, 512, 512);                                             // Limpiar el lienzo
    contexto2.clearRect(0, 0, 512, 512);                                            // Limpiar el lienzo 2
    contextoplataformas.clearRect(0, 0, 512, 512);                                  // Limpiar las plataformas
    contextoplataformas.drawImage(imagennivel, 0 - desfase_global_x, 0, 2048, 512); // Dibujar plataformas

if (jugador.x + desfase_global_x > 400 && desfase_global_x < anchoNivel - 512) {    // Detectar si el jugador está cerca del borde y activar el desplazamiento
    desfase_global_x += 1;                                                          // Reducir la velocidad del desplazamiento
}
if (jugador.x + desfase_global_x < 120 && desfase_global_x > 0) {
    desfase_global_x -= 1;                                                          // Reducir la velocidad del desplazamiento en sentido contrario
}

if (desfase_global_x >= anchoNivel - 512 && !jugador.muerto && !victoriaMostrada) {
    victoriaMostrada = true;                                                        // Has ganado
    setTimeout(() => {
      mensajeActivo = true;                                                         // Activar el mensaje después de 5 segundos
      setTimeout(() => {
        window.location.reload();                                                   // Reiniciar el juego después de otros 3 segundos
      }, 3000);
    }, 5000);                                                                       // Espera 5 segundos antes de mostrar el mensaje
}

if (mensajeActivo) {                                                                // Si el mensaje está activo, mostrar "¡Has ganado!" estilizado
    contexto.clearRect(0, 0, 512, 512);                                             // Limpiar la pantalla
    contexto.font = "bold 40px 'Arial Unicode MS', sans-serif";                     // Fuente estilizada
    contexto.textAlign = "center";                                                  // Centrar el texto horizontalmente
    contexto.fillText("🎉 ¡Has ganado! 🎉", 256, 256);                               // Mensaje 
    return;                                                                         // Salir del bucle mientras el mensaje está en pantalla
}
// Mover y dibujar NPCs
for (let i = 0; i < misnpcs.length; i++) {
    misnpcs[i].mueve();
    misnpcs[i].rebota();
    misnpcs[i].dibuja();

    if (isCollision(jugador, misnpcs[i])) {                                         // Verificar colisión entre el jugador y los NPCs
        window.location.reload();                                                   // Recargar la página si el jugador choca con un NPC
    }
}

// Mover y dibujar balas
for (let i = 0; i < balas.length; i++) {
    balas[i].mueve();
    balas[i].dibuja();

    
    if (balas[i].colisionaConPlataforma()) {                                         // Verificar colisión de la bala con las plataformas
          balas.splice(i, 1);                                                        // Eliminar la bala si colisiona con una plataforma
          i--;                                                                       // Ajustar el índice después de eliminar la bala
    }
}

// Verificar si las balas colisionan con los NPCs
for (let i = 0; i < balas.length; i++) {
    for (let j = 0; j < misnpcs.length; j++) {
        if (calculateDistance(balas[i].x, balas[i].y, misnpcs[j].x, misnpcs[j].y) < 20) {
            misnpcs.splice(j, 1);                                                    // Eliminar NPC si es alcanzado por la bala
            }
    }
}

// Mover y dibujar el jugador
jugador.mueve();
jugador.dibuja();

requestAnimationFrame(bucle); // Usamos requestAnimationFrame para continuar con el bucle
}

// Función que comprueba si hay colisión entre el jugador y un NPC
function isCollision(jugador, npc) {
    const distanciaDeColision = 20;                                                   // Definimos el radio de colisión
    const distancia = calculateDistance(jugador.x, jugador.y, npc.x, npc.y);          // Calculamos la distancia entre el jugador y el NPC
    return distancia < distanciaDeColision;                                           // Si la distancia es menor que el radio de colisión, es que ha habido colisión
}

function calculateDistance(x1, y1, x2, y2) {// Función para calcular la distancia entre dos puntos (jugador y NPC)
    const dx = x2 - x1;
    const dy = y2 - y1;
    return Math.sqrt(dx * dx + dy * dy);
}

// Iniciar el bucle de nuevo
bucle();

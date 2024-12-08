var teclasActivas = {}; 
    document.addEventListener("keydown", function (e) {
        teclasActivas[e.key] = true;                     // Marca la tecla como presionada
        if (e.keyCode == 32) {                           // Barra espaciadora para disparar
        console.log("ok disparo");
        balas.push(new Bala());
        }
    });

document.addEventListener("keyup", function (e) {
    teclasActivas[e.key] = false;                        // Marca la tecla como no presionada
});

function actualizarMovimientoJugador() {
    let movimientoX = 0;
    let movimientoY = 0;
    let velocidad = 2;

    if (teclasActivas["ArrowUp"]) movimientoY -= velocidad;
    if (teclasActivas["ArrowDown"]) movimientoY += velocidad;
    if (teclasActivas["ArrowLeft"]) {
        movimientoX -= velocidad;
        jugador.direccion = "izquierda";
    }
    if (teclasActivas["ArrowRight"]) {
        movimientoX += velocidad;
        jugador.direccion = "derecha";
    }

    if (movimientoX !== 0 && movimientoY !== 0) {         // Ajustar velocidad para movimiento diagonal
        movimientoX *= Math.SQRT1_2;                      // Reducir velocidad en diagonal 
        movimientoY *= Math.SQRT1_2;
    }

    if (!jugador.colisionaPlataformas(movimientoX, movimientoY)) {   // Verificar colisiones antes de mover
    jugador.x += movimientoX;
    jugador.y += movimientoY;
    }
}
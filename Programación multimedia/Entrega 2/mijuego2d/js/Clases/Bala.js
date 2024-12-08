class Bala {
  constructor() {
    this.x = jugador.x;                           // La posición x inicial de la bala es la misma posición del jugador
    this.y = jugador.y;                           // La posición y inicial de la bala es la misma posición del jugador
    this.vx = 5;                                  // A la bala se le da una velocidad inicial
        if (jugador.direccion == "izquierda") {
          this.direccion = -1;                    // En ese caso la velocidad de la bala es negativa
        } else {
          this.direccion = 1;                     // En ese caso la velocidad es positiva
        }
  }
    
  mueve() {
    this.x += this.direccion * this.vx;           // Actualiza la posición de la bala
  }
     
  dibuja() {
    contexto.drawImage(burbuja, this.x - desfase_global_x, this.y, 25, 25); // Dibujo la burbuja y aquí puedo ajustar el tamaño si es necesario
  }

  colisionaConPlataforma() {
    let pixel = contextoplataformas.getImageData(this.x - desfase_global_x, this.y, 1, 1).data;
    if (pixel[3] > 0) {                           // Si la transparencia es mayor que 0, significa que tocó una plataforma
      return true;                                // Hay colisión
    }
    return false;                                 // No hay colisión
  }
}
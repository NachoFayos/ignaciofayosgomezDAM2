class Jugador {
    constructor() {
        this.x = 256;
        this.y = 256;
        this.ancho = 65; 
        this.alto = 65; 
        this.direccion = "izquierda";
      }
    mueve() {
        this.muere();
    }

    muere() {
        if (this.y > 512) {
        window.location = window.location;
        }
    }
    
    dibuja() {
        if (this.direccion == "izquierda") {
            contexto.drawImage(imagenbueno, 0, 0, this.ancho, this.alto, this.x - desfase_global_x, this.y, this.ancho, this.alto);
        } else {
            contexto.drawImage(imagenbueno, 65, 0, this.ancho, this.alto, this.x - desfase_global_x, this.y, this.ancho, this.alto);
        }
    }

colisionaPlataformas(dx, dy) {                                              // Puntos clave para colisión en los bordes del personaje
        const puntosColision = [
      { x: this.x + dx, y: this.y + dy },                                   // Esquina superior izquierda
          { x: this.x + dx + this.ancho, y: this.y + dy },                  // Esquina superior derecha
          { x: this.x + dx, y: this.y + dy + this.alto },                   // Esquina inferior izquierda
          { x: this.x + dx + this.ancho, y: this.y + dy + this.alto },      // Esquina inferior derecha
          { x: this.x + dx + this.ancho / 2, y: this.y + dy },              // Centro superior
          { x: this.x + dx + this.ancho / 2, y: this.y + dy + this.alto }   // Centro inferior
        ];

        for (let punto of puntosColision) {                      // Verifica cada punto de colisión
          let pixel = contextoplataformas.getImageData(
            punto.x - desfase_global_x,
            punto.y,
            1,
            1
          );
          if (pixel.data[3] > 0) {
            return true;                  // Si detecta un píxel sólido, hay colisión
          }
        }
            return false;                 // No se encontró ninguna colisión
    }
}
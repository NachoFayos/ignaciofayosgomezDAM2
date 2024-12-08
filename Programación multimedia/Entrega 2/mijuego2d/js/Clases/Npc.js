class Npc {
    constructor() {
        this.x = Math.random() * 2048;                 // Posición aleatoria dentro del ancho total del nivel
        this.y = Math.random() * (512 - 75);           // Posición aleatoria dentro del alto visible del nivel
        this.angulo = Math.random() * Math.PI * 2;     // Ángulo inicial aleatorio
        this.velocidad = 0.5 + Math.random() * 1;      // Velocidad reducida entre 0.5 y 1.5
        this.tamano = 75;                              // Tamaño del NPC aumentado a 75x75 píxeles
    }

    rebota() {
        if (this.x < 0) {                              // Rebote horizontal dentro de los límites del nivel
          this.x = 0;
          this.angulo = Math.PI - this.angulo;         // Cambiar dirección horizontal
        }
        if (this.x > 2048 - this.tamano) {
          this.x = 2048 - this.tamano;                 // Ajuste para el tamaño del NPC
          this.angulo = Math.PI - this.angulo;         // Cambiar dirección horizontal
    }

        if (this.y < 0) {                              // Rebote vertical dentro de los límites visibles
          this.y = 0;
          this.angulo = -this.angulo;                  // Cambiar dirección vertical
        }
        if (this.y > 512 - this.tamano) {
          this.y = 512 - this.tamano;                  // Ajuste para el tamaño del NPC
          this.angulo = -this.angulo;                  // Cambiar dirección vertical
        }
    }

    mueve() {                                          // Movimiento del NPC basado en su ángulo y velocidad
        this.x += Math.cos(this.angulo) * this.velocidad;
        this.y += Math.sin(this.angulo) * this.velocidad;
        this.rebota();                                 // Aseguramos de que el NPC rebota al moverse
    }

    dibuja() {                                         // Dibujar el NPC en la posición ajustada al desfase global
        if (contexto && imagenmalo) {
          contexto.drawImage(
            imagenmalo,
            this.x - desfase_global_x,                 // Ajustar la posición X al desplazamiento del lienzo
            this.y,
            this.tamano,
            this.tamano
          );
        } else {                                       // Dibujar un marcador visual (rectángulo) si la imagen no está cargada
          contexto.fillStyle = "red";
          contexto.fillRect(
            this.x - desfase_global_x,
            this.y,
            this.tamano,
            this.tamano
          );
        }
    }
}
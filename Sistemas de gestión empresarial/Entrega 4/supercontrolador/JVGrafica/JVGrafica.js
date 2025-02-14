class JVGrafica {
    constructor(datos, color, selector, titulo) {
        this.datos = datos;
        this.color = color;
        this.selector = selector;
        this.titulo = titulo;
    }

    tarta() {
        this.dibujarGrafico(false);
    }

    anillo() {
        this.dibujarGrafico(true);
    }

    dibujarGrafico(esAnillo) {
        let anchura = 300, altura = 300;
        let lienzo = document.createElement("canvas");
        lienzo.width = anchura;
        lienzo.height = altura;
        document.querySelector(this.selector).appendChild(lienzo);
        let ctx = lienzo.getContext("2d");

        let total = this.datos.reduce((sum, dato) => sum + dato.valor, 0);
        let anguloInicial = 0;

        this.datos.forEach((dato, index) => {
            let anguloFinal = (dato.valor / total) * Math.PI * 2;
            let color = this.generarColor(index);

            ctx.fillStyle = color;
            ctx.beginPath();
            ctx.moveTo(anchura / 2, altura / 2);
            ctx.arc(anchura / 2, altura / 2, anchura / 2 - 20, anguloInicial, anguloInicial + anguloFinal);
            ctx.closePath();
            ctx.fill();

            if (esAnillo) {
                ctx.fillStyle = "white";
                ctx.beginPath();
                ctx.arc(anchura / 2, altura / 2, 50, 0, Math.PI * 2);
                ctx.fill();
            }

            let anguloTexto = anguloInicial + anguloFinal / 2;
            let x = anchura / 2 + Math.cos(anguloTexto) * (anchura / 2 - 40) / 2;
            let y = altura / 2 + Math.sin(anguloTexto) * (altura / 2 - 40) / 2;
            
            ctx.fillStyle = "black";
            ctx.font = "14px Arial";
            ctx.textAlign = "center";
            ctx.fillText(dato.texto, x, y);
            
            anguloInicial += anguloFinal;
        });

        ctx.fillStyle = "black";
        ctx.font = "18px Arial";
        ctx.textAlign = "center";
        ctx.fillText(this.titulo, anchura / 2, 20);
    }

    generarColor(index) {
        let colores = ["#3498db", "#2ecc71", "#e74c3c", "#f1c40f", "#9b59b6"];
        return colores[index % colores.length];
    }
}


var imagenbueno = new Image();                                          
    imagenbueno.src = "./img/spritesheettortuga.png"                                     
var imagenmalo = new Image()
    imagenmalo.src = "./img/malo1.png"

var burbuja = new Image();                                          
    burbuja.src = "./img/burbuja.png"                                     

var imagenfondo = new Image();
    imagenfondo.src = "./img/fondo.jpg"
    imagenfondo.onload = function(){                                  
    contextofondo.drawImage(imagenfondo,0,0)                  
    }

var imagennivel = new Image();
    imagennivel.src = "./img/nivel1.png"
    imagennivel.onload = function(){
    contextoplataformas.imageSmoothingEnabled = false;
    console.log("imagen cargada")
    contextoplataformas.drawImage(imagennivel,0,0,2048,512) 
    }


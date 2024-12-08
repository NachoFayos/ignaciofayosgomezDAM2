var desfase_global_x = 0;                   // Inicialmente el desfase es de 0

var jugador = new Jugador();                // Copia del jugador

var misnpcs = [];                                                         
var balas = [];
var numeronpc = 2;                          // Número de npc
for(let i = 0;i<numeronpc;i++){             // Recorro el array
misnpcs[i] = new Npc();                     // Para cada elemento, meto una nueva instancia de Npc
}
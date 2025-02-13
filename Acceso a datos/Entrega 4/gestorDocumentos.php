<?php
    class GestorColecciones {
        private $servidor;																																																		 
        private $basededatos;																									 
        private $conexion;	
			
        public function __construct() {																				
            $this->servidor = "mongodb://localhost:27017";																			  
            $this->basededatos = "bat2";																 	  
            $this->conexion = new MongoDB\Driver\Manager($this->servidor);																														
        }
        public function crearColeccion($nombreColeccion) {
            $command = new MongoDB\Driver\Command(["create" => $nombreColeccion]);
            $this->conexion->executeCommand($this->basededatos, $command);
            return "Colección '$nombreColeccion' creada exitosamente.";
        }
        public function eliminarColeccion($nombreColeccion) {
            $command = new MongoDB\Driver\Command(["drop" => $nombreColeccion]);
            $this->conexion->executeCommand($this->basededatos, $command);
            return "Colección '$nombreColeccion' eliminada correctamente.";
        }
    }
?>
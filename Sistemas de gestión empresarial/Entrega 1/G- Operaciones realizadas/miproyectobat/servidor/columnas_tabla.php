<<<<<<< HEAD
<?php
	if(!isset($_GET['tabla'])){
		$tabla = "usuarios";
	}else{
		$tabla = $_GET['tabla'];
	}
	mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);			// Establezco el nivel de retorno de errores de PHP
	$mysqli = mysqli_connect("localhost", "bat3", "bat3", "bat");		// Me conecto a la base de datos
	$query = "
		SHOW COLUMNS in ".$tabla .";
	";										// Compruebo si el usuario enviado existe en la base de datos
	$result = mysqli_query($mysqli, $query);					// Ejecuto la petición contra la base de datos
	$aplicaciones = [];								// Creo un array vacio
	while ($row = mysqli_fetch_assoc($result)) {					// en el caso de que exista
		$aplicaciones[] = $row;							// Añado nueva aplicacioń al array
	}
	echo json_encode($aplicaciones);
	
=======
<?php
	if(!isset($_GET['tabla'])){
		$tabla = "usuarios";
	}else{
		$tabla = $_GET['tabla'];
	}
	mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);			// Establezco el nivel de retorno de errores de PHP
	$mysqli = mysqli_connect("localhost", "bat3", "bat3", "bat");		// Me conecto a la base de datos
	$query = "
		SHOW COLUMNS in ".$tabla .";
	";										// Compruebo si el usuario enviado existe en la base de datos
	$result = mysqli_query($mysqli, $query);					// Ejecuto la petición contra la base de datos
	$aplicaciones = [];								// Creo un array vacio
	while ($row = mysqli_fetch_assoc($result)) {					// en el caso de que exista
		$aplicaciones[] = $row;							// Añado nueva aplicacioń al array
	}
	echo json_encode($aplicaciones);
	
>>>>>>> df403c8 (Actualización de git)
?>
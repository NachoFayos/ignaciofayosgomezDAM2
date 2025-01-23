<?php
		$servidor = "localhost";																			// Le doy los datos de acceso a la base de datos
		  $usuario = "bat2";																		// 
		  $contrasena = "bat2";																	// 
		  $basededatos = "bat2";																// 
	  
		  $conexion = mysqli_connect(
					$servidor, 
					$usuario, 
					$contrasena, 
					$basededatos
				);	
				
				$query = "INSERT INTO registros VALUES
				
			(
				NULL,
				'".$_SERVER['REQUEST_TIME']."',
				'".$_SERVER['REMOTE_ADDR']."',
				'".$_SERVER['HTTP_USER_AGENT']."',
				'".$_SERVER['REQUEST_URI']."',
				''
				
			)
			
												;";											// Formateo una consulta SQL para ver qué campos tienen restricciones
				
			$result = mysqli_query($conexion , $query);		
?>
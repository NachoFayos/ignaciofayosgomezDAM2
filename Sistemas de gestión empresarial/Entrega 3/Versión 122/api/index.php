<?php

include "inc/error.php";

$mysqli = mysqli_connect("localhost", "bat2", "bat2", "bat2");
if(isset($_GET['o'])){
	switch ($_GET['o']) {
		 case "clientes":
		     include "inc/damepedidos.php";
		     break;
		 case "insertarCliente":
		 		include "inc/insertarcliente.php";
		 		
		 		break;
		 default:
		 	echo "no";
	}
}else{
	echo "no";
}
?>
<?php
header('Access-Control-Allow-Origin: *'); // Permite solicitudes desde cualquier origen
header('Access-Control-Allow-Methods: GET, POST'); // Métodos HTTP permitidos
header('Access-Control-Allow-Headers: Content-Type'); // Encabezados permitidos
header('Content-Type: application/json');


$conexion = new mysqli("localhost", "bat", "bat", "bat");

if ($conexion->connect_error) {
    die(json_encode(["error" => "Conexión fallida: " . $conexion->connect_error]));
}

/////////////////////////////// VERIFICAR TABLAS PERMITIDAS ///////////////////////////////
if (isset($_GET['tabla'])) {
    $tabla = $conexion->real_escape_string($_GET['tabla']);
    $tablas_permitidas = ['clientes', 'inventario', 'departamentos'];

    if (in_array($tabla, $tablas_permitidas)) {
        $query = "SELECT * FROM $tabla";
        $resultado = $conexion->query($query);

        if ($resultado) {
            $datos = [];
            while ($fila = $resultado->fetch_assoc()) {
                $datos[] = $fila;
            }
            echo json_encode($datos, JSON_PRETTY_PRINT);
        } else {
            echo json_encode(["error" => "Error en la consulta: " . $conexion->error]);
        }
    } else {
        echo json_encode(["error" => "Tabla no permitida"]);
    }
} else {
    echo json_encode(["error" => "No se especificó tabla"]);
}

$conexion->close();
?>
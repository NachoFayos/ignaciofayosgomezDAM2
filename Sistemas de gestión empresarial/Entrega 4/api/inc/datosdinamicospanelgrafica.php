<?php
header("Content-Type: application/json");

$conexion = new mysqli("localhost", "bat2", "bat2", "bat2");

$productos = $conexion->query("SELECT estado, COUNT(*) as cantidad FROM productos GROUP BY estado");
$clientes = $conexion->query("SELECT CASE WHEN activo = 1 THEN 'Activos' ELSE 'Inactivos' END as estado, COUNT(*) as cantidad FROM clientes GROUP BY activo");

$data = [
    "productos" => [],
    "clientes" => []
];

while ($row = $productos->fetch_assoc()) {
    $data["productos"][] = ["texto" => $row["estado"], "valor" => (int)$row["cantidad"]];
}

while ($row = $clientes->fetch_assoc()) {
    $data["clientes"][] = ["texto" => $row["estado"], "valor" => (int)$row["cantidad"]];
}

echo json_encode($data);
?>
w
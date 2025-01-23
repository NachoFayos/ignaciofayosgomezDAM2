<?php

/*function sanear($elemento) {
    // Registra la entrada recibida
    error_log("Contenido recibido en sanear: " . print_r($elemento, true));

    if (is_string($elemento)) {
        $elemento = json_decode($elemento, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            error_log("Error al decodificar JSON: " . json_last_error_msg());
            die('{"resultado":"error: entrada no es un JSON válido"}');
        }
    }

    if (!is_array($elemento)) {
        error_log("La entrada no es un arreglo después de validar.");
        die('{"resultado":"error: entrada inválida, no es un arreglo"}');
    }

    $coleccion = ['delete', 'drop', 'truncate', 'table'];
    foreach ($elemento as $clave => $valor) {
        foreach ([$clave, $valor] as $entrada) {
            $entrada = strtolower((string)$entrada);
            if (array_filter($coleccion, fn($palabra) => strpos($entrada, $palabra) !== false)) {
                die('{"resultado":"error: palabra prohibida detectada"}');
            }
        }
    }
    return $elemento;
}*/



?>

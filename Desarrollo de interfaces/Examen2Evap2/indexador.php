<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && !empty($_POST['directorio'])) {
    $directorio_raiz = realpath($_POST['directorio']);
    if ($directorio_raiz === false || !is_dir($directorio_raiz)) {
        echo "<p style='color: red;'>El directorio ingresado no existe o no se puede acceder.</p>";
        exit();
    }
} else {
    $directorio_raiz = __DIR__; // Directorio por defecto
}

function listar_directorios_y_archivos($directorio, $nivel = 0) {
    if (!is_dir($directorio)) {
        echo "<p style='color: red;'>El directorio no existe o no se puede acceder.</p>";
        return;
    }
    
    $archivos = scandir($directorio);
    echo "<ul id='lista-archivos'>";
    
    foreach ($archivos as $archivo) {
        if ($archivo != '.' && $archivo != '..') {
            $ruta_completa = $directorio . DIRECTORY_SEPARATOR . $archivo;
            echo "<li class='archivo-item'>" . str_repeat("&nbsp;&nbsp;&nbsp;", $nivel) . "$archivo</li>";
            if (is_dir($ruta_completa)) {
                listar_directorios_y_archivos($ruta_completa, $nivel + 1);
            }
        }
    }
    
    echo "</ul>";
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indexador de Archivos</title>
    <script>
        function filtrarArchivos() {
            var input, filtro, ul, li, i;
            input = document.getElementById("buscador");
            filtro = input.value.toLowerCase();
            ul = document.getElementById("lista-archivos");
            li = ul.getElementsByTagName("li");
            
            for (i = 0; i < li.length; i++) {
                let texto = li[i].textContent || li[i].innerText;
                if (texto.toLowerCase().includes(filtro)) {
                    li[i].style.display = "";
                } else {
                    li[i].style.display = "none";
                }
            }
        }
    </script>
</head>
<body>
    <h2>Índice de Archivos y Carpetas</h2>
    <form method="POST">
        <label for="directorio">Ingrese el directorio a analizar:</label>
        <input type="text" name="directorio" id="directorio" value="<?php echo htmlspecialchars($directorio_raiz); ?>" required>
        <button type="submit">Analizar</button>
    </form>
    <br>
    <label for="buscador">Buscar archivo:</label>
    <input type="text" id="buscador" placeholder="Escribe para buscar..." onkeyup="filtrarArchivos()">
    <hr>
    <?php listar_directorios_y_archivos($directorio_raiz); ?>
</body>
</html>

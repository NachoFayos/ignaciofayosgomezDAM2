<!doctype html>
<html>
	<head>
		<link rel="Stylesheet" href="estilo.css">
		
	</head>
	<body>
		<form method="POST" action="envia.php"
		action="upload.php" method="post" enctype="multipart/form-data">
			<label>Subir Imagen:</label>
			<input type="file" name="imagen" accept="image/png, image/jpeg">
			<input type="submit" value="Subir">
		<h1><?php echo $_GET['f']; ?></h1>
			<input type="hidden" name="token" value="<?php echo base64_encode(date('U'));?>">
			<input type="hidden" name="formulario" value="<?php echo $_GET['f'];?>">
			<?php

				$archivo = 'forms/'.$_GET['f'].'.json';
				$datos = file_get_contents($archivo);
				$coleccion = json_decode($datos, true);
				foreach($coleccion as $clave=>$valor){
					echo "
					<article>
						<div class='texto'>
							<p><strong>".$valor['titulo']."</strong></p>
							<p>".$valor['descripcion']."</p>
						</div>
						<input 
						type='".$valor['tipo']."' 
						name='".$valor['nombre']."'
						placeholder='".$valor['valorejemplo']."'
						minlength='".$valor['min']."'
						maxlength='".$valor['max']."'";
						if($valor['jvvalidador'] != ""){
						 echo "jvvalidador='".$valor['jvvalidador']."'";
						}
						echo "
						>
					</article>";
				}

			?>
			<input type="submit">
		</form>
		<script>
			<?php echo str_replace(["\r", "\n", "\t"], '', file_get_contents("lib/jvvalidador.js")) ; ?>
		</script>
		<link rel="Stylesheet" href="lib/jvvalidador.css">
	</body>
</html>
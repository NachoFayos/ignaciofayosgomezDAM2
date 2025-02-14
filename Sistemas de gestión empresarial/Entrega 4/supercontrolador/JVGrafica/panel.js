document.addEventListener("DOMContentLoaded", function() {
    // Obtener datos desde el backend (simulado aquí)
    fetch('./api/inc/datosdinamicospanelgrafica.php')
        .then(response => response.json())
        .then(data => {
            new JVGrafica(data.productos, "#3498db", "#graficaProductos", "Productos").tarta();
            new JVGrafica(data.clientes, "#e74c3c", "#graficaClientes", "Clientes").tarta();
        })
        .catch(error => console.error("Error cargando los datos del panel:", error));
});

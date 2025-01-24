const baseUrl = "http://192.168.1.178/GitHub/Segundo/sistemasgestionempresarial/miproyectobat/endpointpublico/api.php";


/////////////////////////////// CLICK DE BOTONES ///////////////////////////////
document.getElementById('botonclientes').addEventListener('click', () => {
    cargardatos('clientes', ['id', 'nombre', 'apellidos', 'email', 'direccion', 'cp', 'poblacion', 'pais']);
});

document.getElementById('botoninventario').addEventListener('click', () => {
    cargardatos('inventario', ['id', 'nombre', 'descripcion', 'precio']);
});

document.getElementById('botondepartamentos').addEventListener('click', () => {
    cargardatos('departamentos', ['id', 'nombre', 'descripcion']);
});

function cargardatos(tabla, headers) {
    const url = `${baseUrl}?tabla=${tabla}`;
    console.log(`Intentando cargar datos desde: ${url}`); 

    fetch(url)
        .then(response => {
            console.log(`Respuesta HTTP: ${response.status}`); // Verificamos el estado HTTP para que todo funcione. 
            return response.json();
        })
        .then(data => {
            console.log(`Datos recibidos:`, data);  
            limpiatabla(headers, data);
        })
        .catch(error => {
            console.error('Error al cargar los datos:', error); // Indicamos un error, para saber si no se están cargando los errores. 
        });
}


function limpiatabla(headers, data) {

    //////////////////////////////// RESETEO DE LA TABLA ///////////////////////////////
    const tableHeaders = document.getElementById('tableHeaders');
    const tableBody = document.getElementById('tableBody');
    tableHeaders.innerHTML = '';
    tableBody.innerHTML = '';

    /////////////////////////////// ENCABEZADOS ///////////////////////////////
    headers.forEach(header => {
        const th = document.createElement('th');
        th.textContent = header;
        tableHeaders.appendChild(th);
    });

    /////////////////////////////// FILAS ///////////////////////////////
    data.forEach(row => {
        const tr = document.createElement('tr');
        Object.values(row).forEach(value => {
            const td = document.createElement('td');
            td.textContent = value;
            tr.appendChild(td);
        });
        tableBody.appendChild(tr);
    });
}

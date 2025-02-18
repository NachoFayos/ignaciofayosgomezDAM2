import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("tienda.db")
cursor = conn.cursor()

# Obtener ventas totales por producto
cursor.execute('''
    SELECT p.nombre, SUM(c.cantidad) as total_vendido
    FROM compras c
    JOIN productos p ON c.producto_id = p.id
    GROUP BY p.nombre
''')

datos = cursor.fetchall()

# Cerrar la conexión
conn.close()

# Verificar si hay datos antes de continuar
if not datos:
    print("⚠️ No se encontraron datos en la tabla `compras`. Verifica que la base de datos tenga información.")
else:
    print("✅ Datos obtenidos con éxito:")
    for producto, cantidad in datos:
        print(f"Producto: {producto} - Cantidad Vendida: {cantidad}")

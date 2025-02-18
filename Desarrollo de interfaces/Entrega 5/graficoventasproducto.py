import sqlite3
import matplotlib.pyplot as plt

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

# Guardar los resultados en la variable datos
datos = cursor.fetchall()

# Cerrar la conexión
conn.close()

# Verificar si hay datos antes de generar el gráfico
if not datos:
    print("⚠️ No hay datos en la base de datos para generar el gráfico.")
else:
    # Extraer nombres de productos y cantidades vendidas
    productos = [row[0] for row in datos]
    ventas = [row[1] for row in datos]

    # Crear el gráfico de barras
    plt.figure(figsize=(8, 5))
    plt.bar(productos, ventas, color='blue')

    # Personalización del gráfico
    plt.xlabel("Productos")
    plt.ylabel("Cantidad Vendida")
    plt.title("Ventas Totales por Producto")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Guardar y mostrar la gráfica
    plt.savefig("ventas_por_producto.png")
    plt.show()

import sqlite3
import matplotlib.pyplot as plt  # Importar matplotlib
import seaborn as sns  # Importar seaborn para mejorar los gráficos

# Conectar a la base de datos
conn = sqlite3.connect("tienda.db")
cursor = conn.cursor()

# Obtener datos de ventas por producto
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

# Verificar si hay datos antes de graficar
if not datos:
    print("No hay datos en la base de datos para generar el gráfico.")
else:
    # Extraer nombres de productos y cantidades vendidas
    productos = [row[0] for row in datos]
    ventas = [row[1] for row in datos]

    # Aplicar el estilo de seaborn
    sns.set_style("whitegrid")

    # Crear el gráfico de barras con seaborn
    plt.figure(figsize=(8, 5))
    sns.barplot(x=productos, y=ventas, palette="Blues_r")

    # Personalización del gráfico
    plt.title("Ventas por Producto - Personalizado", fontsize=14, fontweight='bold', color='darkred')
    plt.xlabel("Productos", fontsize=12, fontweight='bold', color='darkblue')
    plt.ylabel("Cantidad Vendida", fontsize=12, fontweight='bold', color='darkblue')
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)

    # Guardar y mostrar la gráfica
    plt.savefig("ventas_personalizadas.png")
    plt.show()

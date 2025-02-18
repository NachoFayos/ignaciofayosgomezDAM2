import matplotlib.pyplot as plt

# Datos de ejemplo
categorias = ["Enero", "Febrero", "Marzo", "Abril"]
ventas = [1200, 1500, 1800, 2100]

# Crear el gráfico
plt.bar(categorias, ventas, color='blue')

# Personalización
plt.xlabel("Meses")
plt.ylabel("Ventas en USD")
plt.title("Ventas Mensuales")
plt.show()

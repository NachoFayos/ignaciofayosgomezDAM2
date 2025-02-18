import matplotlib.pyplot as plt

# Datos de ejemplo
meses = ["Enero", "Febrero", "Marzo", "Abril"]
ventas = [5000, 7000, 6000, 8000]

# Crear gráfico de barras
plt.bar(meses, ventas, color='blue')

# Personalización
plt.xlabel("Meses")
plt.ylabel("Ventas en USD")
plt.title("Ventas Mensuales")
plt.savefig("Grafico_Ventas.png")  # Guardar gráfico en archivo
plt.show()

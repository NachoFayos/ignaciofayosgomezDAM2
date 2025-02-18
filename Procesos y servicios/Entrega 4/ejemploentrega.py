import matplotlib.pyplot as plt
import pandas as pd

# Cargar datos desde el archivo de logs
datos = pd.read_csv("server_status.log", names=["Fecha", "Estado"], parse_dates=["Fecha"])

# Contar número de veces que el servidor estuvo disponible/no disponible
resumen = datos["Estado"].value_counts()

# Crear gráfico de pastel
plt.figure(figsize=(6, 6))
plt.pie(resumen, labels=resumen.index, autopct="%1.1f%%", startangle=90)
plt.title("Disponibilidad del servidor ERP-CRM")
plt.show()

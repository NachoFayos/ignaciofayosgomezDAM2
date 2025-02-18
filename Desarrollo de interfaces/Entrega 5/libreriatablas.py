import pandas as pd

# Datos de ejemplo
data = {"Producto": ["A", "B", "C"], "Ventas": [1200, 1500, 1800]}
df = pd.DataFrame(data)

# Mostrar tabla en consola
print(df)

# Exportar a Excel
df.to_excel("Reporte_Ventas.xlsx", index=False)

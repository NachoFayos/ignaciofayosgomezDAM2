import sqlite3
import pandas as pd

# Conectar a la base de datos
conn = sqlite3.connect("tienda.db")

# Obtener historial de compras de un cliente
df = pd.read_sql_query("SELECT * FROM compras WHERE cliente_id = 1", conn)

# Mostrar los datos en consola
print(df)

# Exportar a Excel
df.to_excel("Informe_Compras_Cliente.xlsx", index=False)

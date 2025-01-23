import pandas as pd


contenido = pd.read_excel("clientes.xlsx")
diccionario = contenido.to_dict()

print(diccionario)
print(diccionario['nombre'][0])

for clave in diccionario:
    print(clave) #clave te da los nombres de las columnas de la base de datos.

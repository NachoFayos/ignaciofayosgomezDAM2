import csv                                                          # Importo librería para trabajar con CSV
import pandas as pd                                                 # Importo la librería
import mysql.connector                                              # Importo conector de MySQL


############################## CONEXION A MYSQL ################################

conexion = mysql.connector.connect(
            host="localhost",
            database="bat2",
            user="bat2",
            password="bat2"
        )                                                           # Me conecto a la base de datos

cursor = conexion.cursor()                                          # Creo un cursor
peticion = "INSERT INTO clientes (Identificador) VALUES (NULL)"     # Inserto un cliente VACIO
print(peticion)
cursor.execute(peticion)                                            # ejecuto la petición
conexion.commit()                                                   # Lanzo la peticion



############################## CONEXION A MYSQL ################################


############################## CARGO EL MAPEADO DE EXCEL A MYSQL ################################

diccionario = {}                                                    # Creo un diccionario
archivo = open('mapeado.csv', mode='r')                             # Abro el csv en modo lectura
lectorcsv = csv.DictReader(archivo)                                 # Cargo sobre el diccionario el contenido del csv

mapeado = {}                                                        # Creo un diccionario vacía

for fila in lectorcsv:                                              # Para cada una de las filas del csv
    mapeado[fila['excel']] = fila['mysql']                          # Añado el diccionario a la lista

#print(mapeado)                                                      # Lo imprimo para comprobar que todo va bien

############################## CARGO EL MAPEADO DE EXCEL A MYSQL ################################

print("-------------------------------------------")

############################## LEO EXCEL ################################

contenido = pd.read_excel("clientes.xlsx")                          # Leo el contenido del archivo de excel
diccionario = contenido.to_dict()                                   # Lo convierto a diccionario de Python
#print(diccionario)                                                  # imprimo el diccionario

for clave in diccionario:                                           # PAra cada clave en el diccionario
    #print("clave excel:",clave)                                     # Imprimo la clave de excel
    #print("valor de esa clave:",diccionario[clave][0])              # Imprimo su contenido
    #print("La columna coincidente de MySQL es:",mapeado[clave])     # Imprimo la columna correspondiente en MySQL
    #print("--------")                                               # Separador visual
    peticion = "UPDATE clientes SET "+str(mapeado[clave])+" = '"+str(diccionario[clave][0])+"';"
    print(peticion)

############################## LEO EXCEL ################################

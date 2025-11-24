import csv

# Datos que queremos guardar
productos = [
    ["nombre", "precio", "cantidad"],
    ["Pan", 2000, 10],
    ["Leche", 3500, 5],
    ["Huevos", 15000, 30]
]

#Ver si un archivo existe
import os

if os.path.exists("datos.txt"):
    print("Sí existe")

# Crear el archivo CSV
with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerows(productos)

print("Archivo CSV creado correctamente.")
#crea el archivo inventario.csv




#leer un csv fila por fila   1
import csv

with open("inventario.csv", "r", encoding="utf-8") as archivo:
    reader = csv.reader(archivo)

    for fila in reader:
        print(fila)


#leer un csv como diccionario   2

import csv

with open("inventario.csv", "r", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)

    for fila in reader:
        print(fila["nombre"], fila["precio"], fila["cantidad"])


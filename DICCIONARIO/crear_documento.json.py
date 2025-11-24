import json

# Datos como diccionario
inventario = {
    "productos": [
        {"nombre": "Pan", "precio": 2000, "cantidad": 10},
        {"nombre": "Leche", "precio": 3500, "cantidad": 5},
        {"nombre": "Huevos", "precio": 15000, "cantidad": 30}
    ]
}

# Crear archivo JSON
with open("inventario.json", "w", encoding="utf-8") as archivo:
    json.dump(inventario, archivo, indent=4, ensure_ascii=False)

print("Archivo JSON creado correctamente.")


#leer un json

import json

with open("inventario.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print(datos)

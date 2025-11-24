diccionario={
    "nombre":"Juliana",
    "edad":20,
    "ciudad":"Itagui"
}

#modificar
diccionario["edad"]=22
print(diccionario)

#eliminar
del diccionario["ciudad"]
print(diccionario)

#agregar
diccionario["color"]="rojo"
print(diccionario)
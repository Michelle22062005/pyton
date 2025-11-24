casa=("puerta", "ventana","cama")
casa2=("cocina", "nevera")

#acceder a sus elemetos
print(casa[1])

#Recorrer con un bicle

for i in casa:
    print(i)
    
#unir tuplas

resultado= casa + casa2
print(resultado)

#repetirla
print(casa * 3)

#obtener su longitud
num=len(casa)
print(num)

#convertir la tupla en lista para modificarla
lista=list(casa)
lista.append(4)
casa =tuple(lista)
print(casa)

import csv


def login_admin(user_logged_in,password_entered, path_csv="admin_access.csv"):
    with open(path_csv, "r", encoding="utf-8") as archivo:
        reader=csv.DictReader(archivo)
    
        for fila in reader:
            if fila["username"]==user_logged_in and fila["password"] ==password_entered:
                    return True
    return False

user=input("Ingre el ID de administrador: ")
password=input("Ingrese la contraseña: ")
if login_admin(user, password):
        print("Acceso permitido")
else:
        print("Acceso denegado")


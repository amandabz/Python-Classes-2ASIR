# comprobar que una contraseña tiene mínimo 8 caracteres
# comprobar que una contraseña no tiene espacios en blanco

def confirmPassword():

    password = input("Escriba su contraseña: ")
    print(password)

    if len(password) >= 8:
        if " " in password:
            print("Contraseña incorrecta. Hay espacios en blanco.")
        else: 
            print("Contraseña correcta.")
    else:
        print("Contraseña incorrecta. Tiene que tener mínimo 8 caracteres y no tener espacios en blanco")


confirmPassword()
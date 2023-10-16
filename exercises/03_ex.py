# sacar por pantalla: el identificador de ipasen

def ipasen_identificator():

    # print(nombre)
    nombre = input("Escriba su nombre (sin apellidos): ")

    # print(apellidos)
    apellidos = input("Escriba ambos apellidos: ")

    # print(dni)
    dni = input("Escriba su DNI completo: ")

    nombre = nombre[0]
    apellidos = apellidos.split()
    apellido1 = apellidos[0]
    apellido2 = apellidos[1]

    identificador = (nombre + apellido1[:3] + apellido2[:3] + dni[5:8] + "@g.educaand.es").lower() 

    print(identificador)


ipasen_identificator()

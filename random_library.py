# random library
import random  # importamos la librería "random"


age = random.randrange(0, 30)  # printea un numero aleatorio entre el 1 y el 30
print("Edad: " + str(age))
if age >= 18:
    print("Access allowed")
else:
    print("Access denied")


# 100 numeros aleatorios
# dividir en 2 listas de mayor y menor de edad
# no repetir números
# ordenador de menor a mayor (.sort)

legaL_age = []
ilegal_age = []


def legal_and_ilegal_ages():
    for i in range(101):  # printea 100 valores
        value = random.randrange(0, 101)

        if value >= 18:
            if value not in legaL_age:
                legaL_age.append(value)
                legaL_age.sort(reverse=False)  # reverse=False : orden descendente

        else:
            if value not in ilegal_age:
                ilegal_age.append(value)
                ilegal_age.sort(reverse=False)  # reverse=False : orden descendente

    print("Mayores de edad: " + str(legaL_age))
    print("Menores de edad: " + str(ilegal_age))


legal_and_ilegal_ages()


# Sacar 2 listas de números pares e impares
# Ordenadas descendentemente
# No repetirse números

even_list_number = []  # even = par
odd_list_number = []  # odd = impar


def even_and_odd_numbers():
    for i in range(101):  # printea 100 valores
        value = random.randrange(0, 101)

        if value % 2 == 0:
            if value not in even_list_number:
                even_list_number.append(value)

        else:
            if value not in odd_list_number:
                odd_list_number.append(value)

    # saco los .sort fuera del for para que no se ordenen en bucle y solo lo hagan 1 vez
    odd_list_number.sort(reverse=False)  # reverse=False : orden descendente
    even_list_number.sort(reverse=False)  #

    print("Even: " + str(even_list_number))
    print("Odd: " + str(odd_list_number))


even_and_odd_numbers()


# valores aleatorios entre 100 y 1000 (segundos)
# times = ["mm:ss"]

times = []


def minutes_and_seconds():
    for i in range(10):  # printea 10 valores
        value = random.randrange(100, 1000)
        minutes = value // 60
        seconds = value % 60

        time = str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
        times.append(time)

    print("Horas: " + str(times))


minutes_and_seconds()













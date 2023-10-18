# Elige un número entre el 1-100
# Frío si hay > 10 de diferencia
# Caliente si hay < 10 de diferencia

import random


def cold_and_hot_number():

    random_value = random.randrange(1, 100)
    print(random_value)

    number = -1
    attemps = 0

    while random_value != number:

        number = int(input("Introduce un número entre el 1 y el 100: "))
        attemps += 1  # ya hay 1 intento porque ya ha preguntado
        difference = abs(number - random_value)

        if number > 100:
            print("Has introducido un número mayor al rango establecido. Introduce un número entre el 1 y el 100: ")

        elif number == random_value:
            print("¡Acertaste en " + str(attemps) + " intentos!")
            break

        elif difference <= 10:
            print("Caliente...")

        else:
            print("Frío...")


cold_and_hot_number()

import random
import datetime


def guess_function_with_attemps_and_time_spend():
    random_value = random.randrange(1, 100)
    # print(random_value)

    number = 0
    attempts = 0

    # time spend
    start_time = datetime.datetime.now()

    while random_value != number:

        # attempts used
        number = int(input("Introduce un número entre el 1 y el 100: "))
        attempts += 1
        number_difference = abs(number - random_value)

        # time spend
        end_time = datetime.datetime.now()
        time_difference = end_time - start_time
        minutes = time_difference.total_seconds() // 60
        seconds = time_difference.total_seconds() % 60

        if number == random_value:
            print(f"¡Acertaste en {attempts} intentos y has tardado {int(minutes)} minutos y {int(seconds)} segundos!")
            break

        elif number > 100:
            print("Has introducido un número mayor al rango establecido. Introduce un número entre el 1 y el 100: ")

        elif number_difference <= 10:
            print("Caliente...")

        else:
            print("Frío...")


guess_function_with_attemps_and_time_spend()

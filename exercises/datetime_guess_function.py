import random
import datetime


def guess_function_with_attemps_and_time():
    random_value = random.randrange(1, 100)
    print(random_value)

    number = -1
    attempts = 0
    start_time = datetime.datetime.now()

    while random_value != number:

        # attempts used
        number = int(input("Introduce un número entre el 1 y el 100: "))
        attempts += 1
        number_difference = abs(number - random_value)

        # time spend
        end_time = datetime.datetime.now()
        time_difference = end_time - start_time
        formatted_time = str(time_difference).split(".")[0]

        if number == random_value:
            print(f"¡Acertaste en {attempts} intentos y has tardado {formatted_time}!")
            break

        elif number > 100:
            print("Has introducido un número mayor al rango establecido. Introduce un número entre el 1 y el 100: ")

        elif number_difference <= 10:
            print("Caliente...")

        else:
            print("Frío...")


guess_function_with_attemps_and_time()

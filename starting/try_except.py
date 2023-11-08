"""try:
    num_to_sum = 10
    num = int(input("Introduce un número: "))
    num_to_sum += num
    print(f"Tú número + 10 es: {num_to_sum}")

except ValueError:
    print("An Error ocurred")

else:
    print("Nothing went wrong")"""


age = 0


def ask_age():

    age_question = int(input("Introduce tú edad: "))
    return age_question


while not age:
    try:
        age = ask_age()

    except ValueError:
        print("No has introducido un número entero")
        int(input("Vuelve a intentarlo: "))

    else:
        print(f"Tú edad es {age}")
        break

    finally:
        print(age)
        print("---------")


ask_age()

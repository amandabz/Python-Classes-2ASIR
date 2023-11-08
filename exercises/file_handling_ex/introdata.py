import datetime


def add_student_to_students_file():

    today_date = datetime.datetime.now()

    while True:
        question = input("Add new student? (Y/N): ").strip().upper()

        if question not in ["Y", "N"]:
            print("Please enter Y or N.")
            continue

        elif question == "N":
            break

        else:

            name = input("Name: ")
            surname = input("Surname: ")
            dni = input("DNI: ")
            born_date = input("Born date (dd/mm/yyyy): ")

            # check if the ID already exists in the file
            dni_exists = False

            with open("students.txt", "r") as file:
                lines = file.readlines()

                for line in lines:
                    if f"ID: {dni}" in line:
                        dni_exists = True
                        break

            if dni_exists:
                print("This ID already exists in the file. Please enter a different one.")
            else:
                with open("students.txt", "a") as file:
                    file.write(f"""New Student:
Name: {name}
Surname: {surname}
ID: {dni}
Born date: {born_date}
\n
""")

                print("Student added")

                with open("access.log", "a") as log_file:
                    log_file.write(f"""{today_date}:
Student {name} with ID number {dni} added to the student file.
\n""")


add_student_to_students_file()

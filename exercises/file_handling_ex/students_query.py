"""
Al introducir el ID me tiene que aparecer por pantalla:
    STUDENT QUERY:
        Surname, name:
        Age:

    Another query (Y/N):

Si N -> END
Si Y: -> Volver a introducir un DNI
"""

from datetime import datetime


def search_studends_in_students_file():

    today_date = datetime.now()

    with open("students.txt", "r") as file:
        lines = file.readlines()

    while True:
        question = input("Do you want to search a student? (Y/N): ").strip().upper()

        if question not in ["Y", "N"]:
            print("Please enter Y or N.")
            continue

        elif question == "N":
            break

        else:
            dni_to_search = input("Enter a DNI to search: ").strip().upper()
            is_found = False

            for index, line in enumerate(lines):
                if f"ID: {dni_to_search}" in line:
                    is_found = True

                    info = lines[index -2:index +2]
                    name = info[0].split(":")[-1].strip()
                    surname = info[1].split(":")[-1].strip()

                    born_date_year = info[3][-5:].strip()
                    today_year = datetime.now().year
                    age = today_year - int(born_date_year)

                    print(f"""STUDENT QUERY:
    Surname, name: {surname}, {name}
    Age: {age}
    """)
                    with open("access.log", "a") as log_file:
                        log_file.write(f"""{today_date}:
Search for the student {name} in the student file.
\n""")

                    break  # when it finds the ID, it stops scrolling through the file

            if not is_found:
                print("It has not been possible found a student with that DNI")


search_studends_in_students_file()

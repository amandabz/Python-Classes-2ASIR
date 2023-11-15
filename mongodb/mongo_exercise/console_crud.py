import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")

# database creation
students_db = myclient["students_db"]

# collection creation
students_col = students_db["students"]


def console_crud_def():
    while True:
        option_choose = input("""
Choose an option:
    1. Create Student
    2. Search Student
    3. Delete Student
    4. Modify Student
    5. Exit
Your option: """).strip()

        if option_choose not in ["1", "2", "3", "4", "5"]:
            print("Please, choose an available option")
            continue

        elif option_choose == "5":
            print("See you soon!")
            break

        elif option_choose == "1":
            print("You are going to create a student")

            name = input("What is the name of the student?: ")
            surname = input("What is the surname of the student?: ")
            dni = input("What is the dni of the student?: ")

            data_dict = {
                    "name": name,
                    "surname": surname,
                    "dni": dni
            }

            students_col.insert_one(data_dict)

            print("Student added")

        elif option_choose == "2":
            print("You are going to search a student")

            dni_to_search = input("Please, enter a DNI to search a student: ")

            dni = {"dni": dni_to_search}
            student_data = students_col.find(dni)  # return the student data with that dni
            for data in student_data:
                print(data)

        elif option_choose == "3":
            print("You are going to delete a student")

            dni_to_delete = input("Please, enter a DNI to delete a student: ")
            dni = {"dni": dni_to_delete}
            students_col.delete_one(dni)

            print("Student deleted")

        elif option_choose == "4":
            print("You are going to modify a student")
            value_to_modify = input("""
Choose one value to modify:
1. Name
2. Surname
3. DNI
Your option: """).strip()

            if value_to_modify not in ["1", "2", "3"]:
                print("Please, choose an available option")
                continue

            else:
                dni_search_to_modify = input("Please, enter a DNI to modify that student: ")

                # verification of the existence of the DNI
                dni_query = {"dni": dni_search_to_modify}
                existing_student = students_col.find_one(dni_query)

                if existing_student:
                    if value_to_modify == "1":
                        print("You are going to modify the student name")
                        new_value_name = input("Please, enter the new name: ")

                        dni_query = {"dni": dni_search_to_modify}
                        update_data = {"$set": {"name": new_value_name}}

                        # update the document with the new name
                        students_col.update_one(dni_query, update_data)

                        print("Student name modified")

                        # print student data after the update
                        modified_student = students_col.find_one({"name": new_value_name})
                        print(f"New data of the modified student: {modified_student}")

                    elif value_to_modify == "2":
                        print("You are going to modify the student surname")
                        new_value_surname = input("Please, enter the new surname: ")

                        dni_query = {"dni": dni_search_to_modify}
                        update_data = {"$set": {"surname": new_value_surname}}

                        # update the document with the new surname
                        students_col.update_one(dni_query, update_data)

                        print("Student surname modified")

                        # print student data after the update
                        modified_student = students_col.find_one({"surname": new_value_surname})
                        print(f"New data of the modified student: {modified_student}")

                    elif value_to_modify == "3":
                        print("You are going to modify the student dni")
                        new_value_dni = input("Please, enter the new DNI: ")

                        dni_query = {"dni": dni_search_to_modify}
                        update_data = {"$set": {"dni": new_value_dni}}

                        # Update the document with the new dni
                        students_col.update_one(dni_query, update_data)

                        print("Student DNI modified")

                        # print student data after the update
                        modified_student = students_col.find_one({"dni": new_value_dni})
                        print(f"New data of the modified student: {modified_student}")

                else:
                    print("There is not a student with that DNI")


console_crud_def()

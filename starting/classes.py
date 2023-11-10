class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_information(self):
        print(f"Name: {self.name}, Age: {self.age}")


# first way
first_person = Person("Juan", 30)

first_person.print_information()

# second way
first_person.name = "Carlos"
first_person.age = 25

first_person.print_information()


# __name__ and __main__
if __name__ == "__main__":
    print("Este script se está ejecutando directamente.")
else:
    print("Este script se ha importado como un módulo en otro script.")


# if __name__ == '__main__':
    # execute when the module is not initialized from an import statement.


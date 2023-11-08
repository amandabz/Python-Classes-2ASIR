# crear lista con []
my_list = ["apple", "orange", "banana"]
print(type(my_list))

# change list items
my_list[1] = "kiwi"  # en la posición 1 cambia su valor por "kiwi"
print(my_list)

# insert items in list
my_list.insert(2, "watermelon") # en la posición 2, añade "watermelon"
print(my_list)

my_list.append("watermelon")  # añade "watermelon" en la última posición siempre
print(my_list)

# remove list items
my_list.remove("banana")
print(my_list)

my_list.pop(0)  # elimina el elemento de la posición 0. Por defecto elimina el último.
print(my_list)

# vaciar la lista (que no borrarla)
my_list.clear()
print(my_list)
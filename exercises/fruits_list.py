# Queremos este mensaje de salida:
# Fruits : 1 - apple ,  2 - banana ,  3 - cherry

fruits = ["apple", "banana", "cherry"]

count = 0
message = ""

"""
for fruit in fruits:

    count += 1
    message += " " + str(count) + " - " + fruit + ","

message = message.rstrip(message[-1])

print(message)
"""

# Otra opción
for x in range(len(fruits)):

    message += str(x+1) + " - " + fruits[x]

    # siempre que la x sea mayor que la longitud -1, añade una coma
    if x < len(fruits)-1:
        message += " , "

print(message)










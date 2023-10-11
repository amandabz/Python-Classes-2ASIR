# here we start with strings

# así se usa para un texto con saltos de línea
a = '''Esto es un texto
de prueba
en python. Clase 27/09/2023
'''
print(a)


# string as array
b = "Hello, World!"
print(b[0])  # [0] : acceder al primer caracter de una cadena de texto

print(b[len(b)-1])

# looping as strings
for x in "banana":  # for ... in : recorre una a una y lo imprime
    print(x)

# string lenght
c = "Hello World!"
print(len(c))  # imprime la longitud de c

# string check
txt = "The best thing in life are free!"
print("free" in txt)  
print("hello" in txt)  

if "free" in txt:
    print("free está en el texto")
else:
    print("free no está en el texto")


if "blue" not in txt:
    print("blue no está en el texto")

# string methods
# slicing
d = "Hello, World!"
print(d[2:5])  # me da desde el caracter 2 al 5
print(d[7:len(d)-1])
print(d[:5])  # me da desde el principio al 5

# upper/lower case
e = "AMANDA Benitez"
print(e.upper())  # todos los caracteres mayusculas
print(e.lower())  # todos los caracteres minusculas

# strip
f = "    abenhid122@g.educaand.es "
print(f.strip())  # quita los espacios de los extremos

# split
g = "CPIFP, Nuevo, (Desglose IES Campanillas)"
print(g.split())  # separa todas las palabras con comillas simples (tipo lista)

h = g.split(" ")
for i in h:
    print(i)
    
# replace
print(g.replace("a", "x",))  # remplaza todas las a por x
print(g.replace("a", "x", 1))  # solo remplaza la primera a por x

# format
# en el archivo 03_ex.py hay otro ejemplo
age = 36
txt = "My name is John, and I am {}" 

print(txt.format(age))  # sustituye las {} con la variable que le pasemos, da igual cual sea su tipo

# capitalize
name = "amanda"
print(name.capitalize())  # pone la primera letra en mayúscula

# count
print(txt.count("name"))  # cuantas veces esta la palabra "name" en la variable txt

# find
print(txt.find("name"))  # en que posición está la palabra "name" en la variable txt
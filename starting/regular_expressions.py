# regular expressions (https://www.w3schools.com/python/python_regex.asp)

import re  # module to use regular expressions

# check if the string starts with "The" and ends with "Spain"
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match")
else:
    print("Not match")


# findall: encuentra todos los caracteres de la 'a' a la 'm' que encuentre en la variable 'txt'
y = re.findall("[a-m]", txt)
print(y)

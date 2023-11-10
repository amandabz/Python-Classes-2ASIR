# https://www.w3schools.com/python/python_lambda.asp

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax --> lambda arguments : expression

lambda_example = lambda a, b, c: a + b + c  # a, b, c (parametres): a + b + c (return)


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

try:
    value = int(input("Write a number to double: "))
    print(mydoubler(value))

except ValueError or TypeError:
    print("You have to introduce a number.")




# here we start with functions
x = "Awesome"


def my_func():
    # x = "Awesome"
    print("Python is " + x)


my_func()


def global_var_func():
    global x  # cambia el valor de la x global por el valor de la x local
    x = "ok"
    print("Python is " + x)


global_var_func()


def my_other_function(number):
    return number + 5


print(my_other_function(5))

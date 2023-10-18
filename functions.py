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


def my_other_function(number) -> int:
    return number + 5


print(my_other_function(5))


def hello():
    print("Hello " + str(i))


for i in range(10):
    hello()


def sum_two_numbers(a, b) -> int:
    """
    Sum two parameters
    :param a:
    :param b:
    :return:
    """
    return a + b


print(sum_two_numbers(3, 5))
print(sum_two_numbers(5, 6))
print(sum_two_numbers(1003, 10023))


def default_value(country="Sweden"):
    """
    Return a default value
    :param country:
    :return:
    """
    return country


print(default_value())
print(default_value("Spain"))


def print_different_lists(different_lists):
    for element in different_lists:
        print(element)


fruits = ["apple", "banana", "cherry"]


print(print_different_lists(fruits))

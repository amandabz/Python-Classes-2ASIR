# Fibonacci Secuence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...]


sequence = [0, 1]


# def
def fibonacci(number):
    """
    Complete the first 15 values of Fibonacci secuence
    :param number:
    :return:
    """

    sum_in_def_sequence = sequence[-1] + sequence[-2]
    sequence.append(sum_in_def_sequence)

    if number != len(sequence):
        fibonacci(number)


fibonacci(15)
print(sequence)


# while
number = 15

while number != len(sequence):

    sum_in_while_sequence = sequence[-1] + sequence[-2]
    sequence.append(sum_in_while_sequence)

print(sequence)





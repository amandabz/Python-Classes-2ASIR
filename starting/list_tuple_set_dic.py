# https://jerrynsh.com/tuples-vs-lists-vs-sets-in-python/

range_tuple = tuple(range(1000))
range_list = list(range(1000))

print(range_tuple.__sizeof__())  # 8024 bytes
print(range_list.__sizeof__())  # 8040 bytes

"""
use Lists:
https://www.w3schools.com/python/python_lists.asp
    - When you need to remove or add new items to your collection of items.

use Tuples:
https://www.w3schools.com/python/python_tuples.asp
    - if your data should or does not need to be changed.

    -  we should use a Tuple instead of a List if we are defining a constant set
       of values and all we are ever going to do with it is itinerate through it.

    - if we need an array of elements to be used as dictionary keys, we can use Tuples.
"""

# set
# https://www.w3schools.com/python/python_sets.asp
#   - are used to store multiple items in a single variable.
#   - is a collection which is unordered, unchangeable, and unindexed.
my_set = {"apple", "banana", "cherry"}

print(my_set)
print(type(my_set))


# dictionary
# https://www.w3schools.com/python/python_dictionaries.asp
#   - are used to store data values in key: value pairs.
#   - is a collection wich is ordered, changeable and do not allow duplicates.

my_dictionary = {
    "name": "Juan",
    "age": 33
}

print(my_dictionary)
print(type(my_dictionary))

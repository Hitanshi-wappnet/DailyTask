import random
import itertools

# 11.Write a Python function that takes two lists and returns True if
# they have at least one common member.


def check_common_element(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False


list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10]
print(check_common_element(list1, list2))


# 12.Write a Python program to print a specified list after
# removing the 0th, 4th and 5th elements.
def final_list(list):
    list.pop(0)
    list.pop(3)
    list.pop(3)
    return list


print(final_list(["Red", "Green", "White", "Black", "Pink", "Yellow"]))


# 13.Write a Python program to generate a 3*4*6 3D array in each element is *.
array = [[["*" for i in range(6)] for j in range(4)] for k in range(3)]
print(array)


# 14.Write a Python program to print the numbers of a specified list after
#  removing even numbers from it.
def remove_even_numbers(list):
    list1 = []
    for number in list:
        if number % 2 == 1:
            list1.append(number)
    return list1


print(remove_even_numbers([2, 3, 4, 5, 9, 6, 44, 66]))


# 15.Write a Python program to shuffle and print a specified list.
def list_shuffle(list):
    random.shuffle(list)
    return list


print(list_shuffle([1, 2, 3, 4]))


"""
16.Write a Python program to generate and print a list of first and
last 5 elements where the values are square of numbers
between 1 and 30 (both included).
"""


def get_list():
    list1 = []
    for i in range(1, 31):
        list1.append(i**2)
    print(list1[:5])  # Print the first Five element of the list
    print(list1[-5:])  # Print the last Five element of the list


get_list()


"""
17.Write a Python program to generate and print a list
except for the first 5 elements,
where the values are square of numbers between 1 and 30 (both included).
"""


def get_newlist():
    list1 = []
    for i in range(1, 31):
        list1.append(i**2)
    print(list1[5:-5])  # Print the element except first and last five elements


get_newlist()


# 18.Write a Python program to generate all permutations of a list in Python.

print(list(itertools.permutations([1, 2, 3])))


# 19.Write a Python program to get the difference between the two lists.
def get_difference(list1, list2):
    diff_list = []
    for i in range(len(list1)):
        diff_list.append(list1[i] - list2[i])
    return diff_list


list1 = [21, 32, 43, 54, 65]
list2 = [10, 11, 12, 13, 14]
print(get_difference(list1, list2))


# 20.Write a Python program access the index of a list.
def access_index(list):
    print("The list is ", list)
    n = input("Enter the element you want to access the index from ")
    index = list.index(n)
    print("The index of ", n, "is", index)


access_index(["Banana", "Apple", "Mango", "Watermelon", "Orange"])

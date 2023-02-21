from collections import Counter
from itertools import product

"""
61.Write a Python program to count the frequency in a given dictionary.
"""


def count_frequency(dictt):
    result = Counter(dictt.values())
    return result


dictt = {
    "V": 10,
    "VI": 10,
    "VII": 40,
    "VIII": 20,
    "IX": 70,
    "X": 80,
    "XI": 40,
    "XII": 20,
}

print("Original Dictionary:")
print(dictt)
print("Count the frequency of the said dictionary:")
print(count_frequency(dictt))


"""
62.Write a Python program to extract values from a given dictionaries and
create a list of lists from those values.
"""


def extract_values(dictt, keys):
    return [list(d[k] for k in keys) for d in dictt]


students = [
    {"student_id": 1, "name": "Prish", "class": "V"},
    {"student_id": 2, "name": "Prisha", "class": "V"},
    {"student_id": 3, "name": "aditi", "class": "VI"},
]

print("\nOriginal Dictionary:")
print(students)
print("Extract values from the dictionary and create a list")
print(extract_values(students, ("student_id", "name", "class")))
print(extract_values(students, ("student_id", "name")))
print(extract_values(students, ("name", "class")))


"""
63.Write a Python program to convert a given list of lists to a dictionary.
"""


def list_to_dict(lst):
    result = {item[0]: item[1:] for item in lst}
    return result


students = [[1, "Shivam", "V"], [2, "Shreya", "V"], [3, "Navya", "VI"]]
print(list_to_dict(students))


"""
64.Write a Python program to create a key-value list pairings
in a given dictionary.
"""


def key_value_pairing(dictt):
    result = [dict(zip(dictt, sub)) for sub in product(*dictt.values())]
    return result


students = {1: ["Shivam"], 2: ["Shreya"], 3: ["Itisha"]}

print("A key-value list pairings of the said dictionary:")
print(key_value_pairing(students))


"""
65.Write a Python program to get the total length of all values of a
given dictionary with string values.
"""


def total_length(dictt):
    result = sum((len(values) for values in dictt.values()))
    return result


color = {"#FF0000": "Red", "#800000": "Maroon", "#FFFF00": "Yellow"}
print("Total length of all values of the said dictionary with string values:")
print(total_length(color))


"""
66.Write a Python program to check if a specific Key and a value
exist in a dictionary.
"""


def check_key_value(dictt, key, value):
    if any(item[key] == value for item in dictt):
        return True
    return False


students = [
    {"student_id": 1, "name": "Prish", "class": "V"},
    {"student_id": 2, "name": "Prisha", "class": "V"},
    {"student_id": 3, "name": "aditi", "class": "VI"},
]
print("Check if a specific Key and a value exist in the said dictionary:")
print(check_key_value(students, "student_id", 1))
print(check_key_value(students, "name", "Shreya"))

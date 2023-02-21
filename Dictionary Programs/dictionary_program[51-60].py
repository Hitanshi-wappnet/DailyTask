import itertools

"""
51.A Python Dictionary contains List as value.
Write a Python program to update the list values in the said dictionary.
"""


def update_list(dictionary):
    dictionary["Math"] = [x + 1 for x in dictionary["Math"]]
    dictionary["Physics"] = [x - 2 for x in dictionary["Physics"]]
    return dictionary


dictionary = {"Math": [88, 89, 90], "Physics": [92, 94, 89]}
print("\nOriginal Dictionary:")
print(dictionary)
print("\nUpdate the list values of the said dictionary:")
print(update_list(dictionary))


"""
52.Write a Python program to extract a list of values from a given
list of dictionaries.
"""


def extract_list(lst, marks):
    result = [d[marks] for d in lst if marks in d]
    return result


marks = [
    {"Math": 90, "Science": 92},
    {"Math": 89, "Science": 94},
    {"Math": 92, "Science": 88},
]

print("Original Dictionary:")
print(marks)
subj = "Science"
print("Extract a list of values where subject =", subj)
print(extract_list(marks, subj))


"""
53.Write a Python program to find the length of a given dictionary values.
"""


def len_values(dict):
    result = {}
    for val in dict.values():
        result[val] = len(val)
    return result


color_dict = {1: "red", 2: "green", 3: "black", 4: "white", 5: "black"}
print("Length of dictionary values:")
print(len_values(color_dict))


"""
54.Write a Python program to get the depth of a dictionary.
"""


def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0


dic = {"a": 1, "b": {"c": {"d": {}}}}
print(dict_depth(dic))


"""
55.Write a Python program to access dictionary key's element by index.
"""


num = {"physics": 80, "math": 90, "chemistry": 86}
print(list(num)[0])
print(list(num)[1])
print(list(num)[2])


"""
56.Write a Python program to convert a given dictionary into a list of lists.
"""


def dic_to_list(dictt):
    result = list(map(list, dictt.items()))
    return result


color_dict = {1: "red", 2: "green", 3: "black", 4: "white", 5: "black"}
print(dic_to_list(color_dict))


"""
57.Write a Python program to filter even numbers from a given dictionary
values.
"""


def remove_even_numbers(dict):
    dict1 = {}
    for key, value in dict.items():
        if value % 2 == 1:
            dict1[key] = value
    return dict1


dict1 = {"data1": 100, "data2": 11, "data3": 18, "data4": 33}
print(remove_even_numbers(dict1))


"""
58.Write a Python program to get all combinations of key-value pairs
in a given dictionary.
"""


def get_combination(dictt):
    result = list(map(dict, itertools.combinations(dictt.items(), 2)))
    return result


students = {"V": [1, 4, 6, 10], "VI": [1, 4, 12], "VII": [1, 3, 8]}
print("Combinations of key-value pairs of the said dictionary:")
print(get_combination(students))


"""
59.Write a Python program to find the specified number of maximum values
in a given dictionary.
"""


def maximum_values(dictt, N):
    result = sorted(dictt, key=dictt.get, reverse=True)[:N]
    return result


dictt = {
    "a": 5,
    "b": 14,
    "c": 32,
    "d": 35,
    "e": 24,
    "f": 100,
    "g": 57,
    "h": 8,
    "i": 100,
}
print("Original Dictionary:")
print(dictt)
N = 1
print(N, "maximum value(s) in the said dictionary:")
print(maximum_values(dictt, N))
N = 2
print(N, "maximum value(s) in the said dictionary:")
print(maximum_values(dictt, N))
N = 5
print(N, "maximum value(s) in the said dictionary:")
print(maximum_values(dictt, N))


"""
60.Write a Python program to find shortest list of values with the keys
in a given dictionary.
"""


def shortest_length(dictt):
    min_value = 1
    result = [k for k, v in dictt.items() if len(v) == (min_value)]
    return result


dictt = {
    "V": [10, 12],
    "VI": [10],
    "VII": [10, 20, 30, 40],
    "VIII": [20],
    "IX": [10, 30, 50, 70],
    "X": [80],
}

print("Shortest list of values with the keys of the said dictionary:")
print(shortest_length(dictt))

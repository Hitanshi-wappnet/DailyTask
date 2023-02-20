import itertools
from collections import Counter

"""
21.Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
"""
d = {"1": ["a", "b"], "2": ["c", "d"]}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print("".join(combo))


"""
22.Write a Python program to find the highest 3 values of
 corresponding keys in a dictionary.
"""


def heighest_value():
    my_dict = {"a": 500, "b": 5874, "c": 560, "d": 400, "e": 920, "f": 20}
    x = list(my_dict.values())
    x.sort(reverse=True)
    x = x[:3]
    for i in x:
        for j in my_dict.keys():
            if my_dict[j] == i:
                print(str(j) + " : " + str(my_dict[j]))


heighest_value()


"""
23.Write a Python program to combine values in python list of dictionaries.
"""
item = [
    {"item": "item1", "amount": 400},
    {"item": "item2", "amount": 300},
    {"item": "item1", "amount": 750},
]
result = Counter()
for d in item:
    result[d["item"]] += d["amount"]
print(result)


"""
24.Write a Python program to create a dictionary from a string
"""


str1 = "Shreya"
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)


"""
25.Write a Python program to print a dictionary in table format.
"""


my_dict = {"C1": [1, 2, 3], "C2": [5, 6, 7], "C3": [9, 10, 11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)


"""
26.Write a Python program to count the values associated with key
in a dictionary.
"""
student = [
    {"id": 1, "success": True, "name": "Lary"},
    {"id": 2, "success": False, "name": "Rabi"},
    {"id": 3, "success": True, "name": "Alex"},
]
print(sum(d["id"] for d in student))


"""
27. Write a Python program to convert a list into a nested dictionary of keys.
"""
list1 = [1, 2, 3, 4]
new_dict = current = {}
for item in list1:
    current[item] = {}
    current = current[item]
print(new_dict)


"""
28.Write a Python program to sort a list alphabetically in a dictionary.
"""
num = {"n1": [2, 3, 1], "n2": [5, 1, 2], "n3": [3, 2, 4]}
sorted_dict = {x: sorted(y) for x, y in num.items()}
print(sorted_dict)


"""
29.Write a Python program to remove spaces from dictionary keys.
"""
product_list = {"P 01": "DBMS", "P 02": "OS", "P 0 3 ": "Soft Computing"}
# removing spaces from keys
# storing them in sam dictionary
product_list = {x.replace(" ", ""): v for x, v in product_list.items()}
print(" New dictionary : ", product_list)


"""
30.Write a Python program to get the top three items in a shop
"""


def heighest_threevalue():
    items = {"item1": 45.50, "item2": 35, "item3": 41.30, "item4": 55,
             "item5": 24}
    y = list(items.values())
    y.sort(reverse=True)
    y = y[:3]
    for i in y:
        for j in items.keys():
            if items[j] == i:
                print(str(j) + " : " + str(items[j]))


heighest_threevalue()

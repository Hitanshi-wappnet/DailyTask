"""
1.Create a dictionary
"""
d = {"Name": "Katha", "job": "Programmer", "company": "earthquone"}
print(d)  # print the dictionary


"""
2.Add Key in Dictionary
"""
d.update({"salary": 100000})
print(d)


"""
3.Write a Python script to concatenate the following
dictionaries to create a new one.
"""
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3):  # concatenate the string
    dic4.update(d)
print(dic4)


"""
4.Write a Python script to check whether a given key
already exists in a dictionary.
"""

dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def key_present(n):
    if n in dict1:  # check whether key is in dictionary or not
        print("Key is present in the dictionary")
    else:
        print("Key is not present in the dictionary")


key_present(4)


"""
5.Write a Python program to iterate over dictionaries using for loops.
"""
# iterate over dictionaries
for dict_key, dict_value in dict1.items():
    print(dict_key, ":", dict_value)


"""
6.Write a Python script to generate and print a dictionary that contains
a number (between 1 and n) in the form (x, x*x).
"""
n = 10
d1 = dict()
for i in range(1, n + 1):
    d1[i] = i * i
print(d1)


"""
7.Write a Python script to print a dictionary
where the keys are numbers between 1 and 15 (both included)
and the values are square of keys.
"""
d2 = dict()
for i in range(1, 16):
    d2[i] = i * i
print(d2)


"""
8.Write a Python script to merge two Python dictionaries.
"""
d3 = {"a": 100, "b": 200}
d4 = {"x": 300, "y": 200}
d5 = d3.copy()  # merge between two dictionaries
d5.update(d4)
print(d5)


"""
9.Write a Python program to iterate over dictionaries using for loops.
"""
for key, value in d2.items():
    print(key, " : ", value)  # iterate over string


"""
10.Write a Python program to sum all the items in a dictionary.
"""
print(sum(d2.values()))  # sum the value

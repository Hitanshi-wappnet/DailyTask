from collections import Counter

"""
11.Write a Python program to multiply all the items in a dictionary.
"""
d1 = {"data1": 100, "data2": 2, "data3": 18}
result = 1
for value in d1:
    result = result * d1[value]  # multiply item

print(result)


"""
12.Write a Python program to remove a key from a dictionary.
"""


def remove_key():
    if "data3" in d1:
        del d1["data3"]  # delete the key from dictionary
        print(d1)


remove_key()


"""
13. Write a Python program to map two lists into a dictionary.
"""
keys = ["1", "2", "3"]
values = ["121", "232", "343"]
d2 = dict(zip(keys, values))  # map two lists in dictionary
print(d2)


"""
14.Write a Python program to sort a dictionary by key.
"""
print("Sorted Dictionary is : ")
for key in sorted(d2):
    print("%s: %s" % (key, d2[key]))  # sorting according to key


"""
15. Write a Python program to get the maximum and minimum value in
 a dictionary.
"""
key_max = max(d1.keys(), key=(lambda k: d1[k]))
key_min = min(d1.keys(), key=(lambda k: d1[k]))
print("Maximum Value: ", d1[key_max])
print("Minimum Value: ", d1[key_min])


"""
16.Write a Python program to get a dictionary from an object's fields.
"""


class dictObj(object):
    def __init__(self):
        self.x = "red"
        self.y = "Yellow"
        self.z = "Green"


test = dictObj()
print(test.__dict__)


"""
17.Write a Python program to remove duplicates from Dictionary.
"""
d2.update({"1": "121"})
result = {}

for key, value in d2.items():  # remove duplicate item
    if value not in result.values():
        result[key] = value

print(result)


"""
18.Write a Python program to check a dictionary is empty or not.
"""
d3 = {}

if not bool(d3):
    print("Dictionary is empty")


"""
19.Write a Python program to combine two dictionary adding values
for common keys.
"""
d4 = {"a": 100, "b": 200, "c": 300}
d5 = {"a": 300, "b": 200, "d": 400}
d = Counter(d4) + Counter(d5)  # add value from common keys
print(d)


"""
20.Write a Python program to print all unique values in a dictionary.
"""
L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}]
print("Original List: ", L)
u_value = set(val for dic in L for val in dic.values())
print("Unique Values: ", u_value)

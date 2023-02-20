from collections import Counter

"""
31.Write a Python program to get the key, value and item in a dictionary.
"""
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
count = 0
print("key  value  count")
for key, value in dict_num.items():
    count = count + 1
    print(key, value, count)


"""
32.Write a Python program to print a dictionary line by line.
"""
for key, value in dict_num.items():
    print(key, " : ", value)


"""
33.Write a Python program to check multiple keys exists in a dictionary.
"""

student = {"name": "Shreya", "class": "12", "roll_id": "2"}
print(student.keys() >= {"class", "name"})
print(student.keys() >= {"name", "Shreya"})
print(student.keys() >= {"roll_id", "name"})


"""
34.Write a Python program to count number of items in a dictionary
value that is a list.
"""


def check_list():
    dict = {"Rollno": ["1", "2", "3"], "Name": ["Shreya", "Shivam"]}
    c = sum(map(len, dict.values()))
    print(c)


check_list()


"""
35.Write a Python program to sort Counter by value.
"""
x = Counter({"Math": 81, "Physics": 83, "Chemistry": 87})
print(x.most_common())


"""
36. Write a Python program to create a dictionary from two lists
without losing duplicate values.
"""


def list_to_dict():
    test_keys = ["Shreya", "Shivam", "Divyani"]
    test_values = [1, 4, 5]

    res = {}
    for key in test_keys:
        for value in test_values:
            res[key] = value
            test_values.remove(value)
            break
    print("Resultant dictionary is : " + str(res))


list_to_dict()


"""
37.Write a Python program to replace dictionary values with their average.
"""


def value_with_avg(list_of_dicts):
    for item in list_of_dicts:
        n1 = item.pop("V")
        n2 = item.pop("VI")
        item["V+VI"] = (n1 + n2) / 2
    return list_of_dicts


student_details = [
    {"id": 1, "subject": "math", "V": 70, "VI": 82},
    {"id": 2, "subject": "math", "V": 73, "VI": 74},
    {"id": 3, "subject": "math", "V": 75, "VI": 86},
]
print(value_with_avg(student_details))

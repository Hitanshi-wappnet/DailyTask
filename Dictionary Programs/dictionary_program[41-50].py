"""
41.Write a Python program to drop empty Items from a given Dictionary.
"""


def drop_empty_item(dic):
    dic1 = {}
    for k, v in dic.items():
        if v is not None:
            dic1[k] = v
    print(dic1)


d1 = {"c1": "Red", "c2": "Green", "c3": None}
drop_empty_item(d1)


"""
42.Write a Python program to filter a dictionary based on values.
"""


def filter_dictionary():
    my_dict = {"a": 500, "b": 5874, "c": 560, "d": 400, "e": 920, "f": 20}
    x = list(my_dict.values())
    x.sort(reverse=True)
    x = x[:3]
    for i in x:
        for j in my_dict.keys():
            if my_dict[j] == i:
                print(str(j) + " : " + str(my_dict[j]))


filter_dictionary()


"""
43.Write a Python program to convert more than one list to nested dictionary.
"""


def nested_dictionary(l1, l2, l3):
    result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
    return result


student_id = ["S001", "S002", "S003", "S004"]
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
student_grade = [85, 98, 89, 92]
print(nested_dictionary(student_id, student_name, student_grade))


"""
44.Write a Python program to filter the height and width of students,
which are stored in a dictionary.
"""


def filter_data(students):
    result = {k: s for k, s in students.items() if s[0] >= 6.0 and s[1] >= 70}
    return result


students = {
    "Shreya": (6.2, 70),
    "Shivam": (5.9, 65),
    "Itisha": (6.0, 68),
    "Riya": (5.8, 66),
}
print("Height > 6ft and Weight> 70kg:")
print(filter_data(students))


"""
45.Write a Python program to check all values are same in a dictionary.
"""


def check_value(students, n):
    result = all(x == n for x in students.values())
    return result


students = {"Shreya": 12, "Shivam": 12, "Itisha": 12, "Riya": 12}
n = 12
print(check_value(students, n))


"""
46.Write a Python program to create a dictionary grouping a sequence of
key-value pairs into a dictionary of lists.
"""


def grouping_dictionary(d):
    result = {}
    for k, v in d:
        result.setdefault(k, []).append(v)
    return result


colors = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
print(grouping_dictionary(colors))


"""
47.Write a Python program to split a given dictionary of lists into
list of dictionaries.
"""


def list_of_dictionaries():
    test_dict = {"Shreya": [1, 3], "Manjeet": [1, 4], "Akash": [3, 4]}
    # using list comprehension
    # to convert dictionary of list to
    # list of dictionaries
    res = [{key: value[i] for key, value in test_dict.items()}
           for i in range(2)]

    # printing result
    print("The converted list of dictionaries " + str(res))


"""
48.Write a Python program to remove a specified dictionary from a given list.
"""


def remove_dictionary(colors, r_id):
    colors[:] = [d for d in colors if d.get("id") != r_id]
    return colors


colors = [
    {"id": "#FF0000", "color": "Red"},
    {"id": "#800000", "color": "Maroon"},
    {"id": "#FFFF00", "color": "Yellow"},
    {"id": "#808000", "color": "Olive"},
]
print("Original list of dictionary:")
print(colors)
r_id = "#FF0000"
print("Remove id", r_id, "from the said list of dictionary:")
print(remove_dictionary(colors, r_id))


"""
49.Write a Python program to convert string values of a given dictionary,
into integer/float datatypes.
"""


def convert_to_int(lst):
    result = [dict([a, int(x)] for a, x in b.items()) for b in lst]
    return result


def convert_to_float(lst):
    result = [dict([a, float(x)] for a, x in b.items()) for b in lst]
    return result


nums = [{"x": "10", "y": "20", "z": "30"}, {"p": "40", "q": "50", "r": "60"}]
print("Converted to Integers: ", convert_to_int(nums))
print("Converted to Float: ", convert_to_float(nums))


"""
50.A Python Dictionary contains List as value. Write a Python program
to clear the list values in the said dictionary.
"""


def remove_list(dictionary):
    for key in dictionary:
        dictionary[key].clear()
    return dictionary


dictionary = {"C1": [10, 20, 30], "C2": [20, 30, 40], "C3": [12, 34]}
print("Original Dictionary:")
print(dictionary)
print("Clear the list values in the said dictionary:")
print(remove_list(dictionary))

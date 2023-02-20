import textwrap
import difflib

"""
81.Write a Python program to find the index of a given
string at which a given substring starts.
If the substring is not found in the given string return 'Not found'.
"""


def index_of_substring(string, substring):
    if len(substring) > len(string):
        return "Not found"
    for i in range(len(string)):
        for j in range(len(substring)):
            if string[i + j] == substring[j] and j == len(substring) - 1:
                return i
            elif string[i + j] != substring[j]:
                break
    return "Not found"


print(index_of_substring("Welcome", "co"))


"""
82.Write a Python program to wrap a given string into a paragraph of
given width.
"""


def wrap_into_string(string):
    width = 10
    print(textwrap.fill(string, width))


wrap_into_string(" The quick brown fox.")


"""
83.Write a Python program to print four values decimal, octal,
hexadecimal (capitalized), binary in a single line of a given integer.
"""
i = 18
o = str(oct(i))[2:]
h = str(hex(i))[2:]
h = h.upper()
b = str(bin(i))[2:]
d = str(i)
print("Decimal,Octal ,Hexadecimal (capitalized), Binary")
print(d, " ", o, " ", h, " ", b)


"""
84.Write a Python program to swap cases of a given string.
"""


def swap_cases(string):
    new_string = ""
    for item in string:
        if item.isupper():
            new_string = new_string + item.lower()
        elif item.islower():
            new_string = new_string + item.upper()
    return new_string


print(swap_cases("HitaNshi"))


"""
85.Write a Python program to convert a given Bytearray to Hexadecimal string.
"""


def bytearray_to_hexadecimal(list):
    result = "".join("{:02x}".format(x) for x in list)
    return result


list = [111, 12, 45, 67, 109]
print(bytearray_to_hexadecimal(list))


"""
86.Write a Python program to delete all occurrences
of a specified character in a given string.
"""


def delete_character(string, n):
    for i in string:
        if i == n:
            string = string.replace(i, "")
    return string


print(
    delete_character(
     "Delete all occurrences of a specified character in a given string", "a"
    )
)


"""
87.Write a Python program find the common values that appear in
two given strings.
"""


def common_value(string1, string2):
    new_str = ""
    for i in string1:
        if i in string2:
            new_str = new_str + i
    print(new_str)


str1 = "abcdef"
str2 = "efgh"
common_value(str1, str2)


"""
88.Write a Python program to check whether a given string
contains a capital letter, a lower case letter, a number and a minimum length.
"""


def check_string(string):
    messg = [
        lambda str1: any(x.isupper() for x in str1),
        lambda str1: any(x.islower() for x in str1),
        lambda str1: any(x.isdigit() for x in str1),
        lambda str1: len(str1) >= 7,
    ]
    result = [x for x in [i(string) for i in messg] if x is not True]
    if not result:
        result.append("Valid string.")
    return result


print(check_string("Hitanshi800"))


"""
89.Write a Python program to remove unwanted characters from a given string.
"""


def remove_unwanted_charactres(string):
    for i in string:
        if i.isalnum():
            continue
        else:
            string = string.replace(i, "")
    return string


print(remove_unwanted_charactres(" A%^!B#*CD"))


"""
90.Write a Python program to remove duplicate words from a given string.
"""


def remove_repeated_word(string):
    list1 = string.split()
    list = []
    for i in list1:
        if i in list:
            list.remove(i)
        else:
            list.append(i)
    new_str = " ".join(list)
    return new_str


print(remove_repeated_word("Hello Mini How are you Mini"))


"""
91.Write a Python program to convert a given heterogeneous
list of scalars into a string.
"""


def heterogeneous_list_to_str(lst):
    result = ",".join(str(x) for x in lst)
    return result


list = ["Red", 100, -50, "green", "w,3,r", 12.12, False]
print(heterogeneous_list_to_str(list))


"""
92.Write a Python program to find the string similarity
between two given strings.
"""


def string_similarity(str1, str2):
    result = difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
    return result.ratio()


str1 = "Python Exercises"
str2 = "Python Exercises"
string1 = "Python Exercises"
string2 = "Pyth Exercise"
print(string_similarity(str1, str2))
print(string_similarity(string1, string2))

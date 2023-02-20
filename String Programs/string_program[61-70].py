import re
from collections import Counter

"""
61. Write a Python program to remove duplicate characters of a given string.
"""


def remove_duplicate_characters(string):
    list = []
    for i in string:
        if i not in list:
            list.append(i)
    for item in range(len(list)):
        print(list[item], end="")
    print()


remove_duplicate_characters("Hello how are you")


"""
62.Write a Python program to compute sum of digits of a given string.
"""


def compute_sum(string):
    list = []
    sum = 0
    for i in string:
        if ord(i) > 46 and ord(i) < 58:
            list.append(i)
    for item in range(len(list)):
        sum = sum + int(list[item])
    print(sum)


compute_sum("1254lkmn2563")


"""'
63.Write a Python program to remove leading zeros from an IP address.
"""
ip = "216.08.094.196"
string = re.sub(r"\.[0]*", ".", ip)
print(string)


"""
64.Write a Python program to find maximum length of
consecutive 0's in a given binary string.
"""


def max_len_zero(string):
    return max(map(len, string.split("1")))


print(max_len_zero("0000100000111"))


"""
65. Write a Python program to find all the common characters in
lexicographical order from two given lower case strings.
If there are no common letters print "No common characters".
"""


def common_characters(str1, str2):
    d1 = Counter(str1)
    d2 = Counter(str2)
    common_dict = d1 & d2
    if len(common_dict) == 0:
        return "No common characters."
    # list of common elements
    common_chars = list(common_dict.elements())
    common_chars = sorted(common_chars)

    return "".join(common_chars)


str1 = "abcde"
str2 = "fgeac"
print(common_characters(str1, str2))


"""
66.Write a Python program to make two given strings
(lower case, may or may not be of the same length)
anagrams removing any characters from any of the strings.
"""
pass


"""
67.Write a Python program to remove all consecutive duplicates
of a given string.
"""


def consecutive_repeat(string):
    list = []
    for i in string:
        if i not in list:
            list.append(i)
    return "".join(list)


print(consecutive_repeat("abbbcdd"))


"""
68.Write a Python program to create two strings from a given string.
Create the first string using those character which
occurs only once and create the second string
which consists of multi-time occurring characters in the said string.
"""


def generateStrings(input):
    str_char = Counter(input)
    part1 = [key for (key, count) in str_char.items() if count == 1]
    part2 = [key for (key, count) in str_char.items() if count > 1]
    part1.sort()
    part2.sort()
    return part1, part2


input = "abbbccdde"
s1, s2 = generateStrings(input)
print("".join(s1))
print("".join(s2))

"""
69.Write a Python program to find the longest common sub-string
from two given strings.
"""


def longest_common(string1, string2):
    max_length = 0
    list1 = string1.split()
    list2 = string2.split()
    list = []
    for i in list1:
        if i in list2:
            list.append(i)
    for ele in list:
        if len(ele) > max_length:
            max_element = ele
        return max_element


str1 = "Hello How are you Mini"
str2 = "Hello Mini I am back"
print(longest_common(str1, str2))


"""
70.Write a Python program to create a string from
two given strings concatenating uncommon characters of the said strings.
"""


def concatenate(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    list3 = []
    for i in list1:
        if i not in list2:
            list3.append(i)
    for j in list2:
        if j not in list1:
            list3.append(j)
    new_str = "".join(list3)
    print(new_str)


str1 = "abcdef"
str2 = "efgh"
concatenate(str1, str2)

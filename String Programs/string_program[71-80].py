"""
71.Write a Python program to move all spaces to the front of a
given string in single traversal.
"""


def moveSpaces(str):
    no_spaces = [char for char in str if char != " "]
    space = len(str) - len(no_spaces)
    # Create string with spaces
    result = " " * space
    return result + "".join(no_spaces)


s1 = "abcd efgh"
print(moveSpaces(s1))


"""
72.Write a Python code to remove all characters except
a specified character in a given string.
"""


def remove_characters(string, n):
    return "".join([el for el in string if el == n])


print(remove_characters("hitanshi", "h"))


"""
73.Write a Python program to count Uppercase, Lowercase,
special character and numeric values in a given string.
"""


def count(str):
    upper, lower, number, special = 0, 0, 0, 0
    for i in range(len(str)):
        if str[i] >= "A" and str[i] <= "Z":
            upper += 1
        elif str[i] >= "a" and str[i] <= "z":
            lower += 1
        elif str[i] >= "0" and str[i] <= "9":
            number += 1
        else:
            special += 1
    print("The upper characters are: ", upper)
    print("The lower characters are: ", lower)
    print("The number characters are: ", number)
    print("The special characters are: ", special)


count("ABcde1234#")


"""
74.Write a Python program to find the minimum window in a given string
which will contain all the characters of another given string.
"""
pass


"""
75.Write a Python program to find smallest window that
contains all characters of a given string.
"""
pass


"""
76.Write a Python program to count number of substrings
from a given string of lowercase alphabets
with exactly k distinct (given) characters.
"""


def count_k_dist(str1, k):
    str_len = len(str1)
    result = 0
    ctr = [0] * 27
    for i in range(0, str_len):
        dist_ctr = 0
        ctr = [0] * 27
        for j in range(i, str_len):
            if ctr[ord(str1[j]) - 97] == 0:
                dist_ctr += 1
            ctr[ord(str1[j]) - 97] += 1
            if dist_ctr == k:
                result += 1
            if dist_ctr > k:
                break
    return result


# str1 = input("Input a string (lowercase alphabets):")
# k = int(input("Input k: "))
# print("Number of substrings with exactly", k, "distinct characters:", end="")
# print(count_k_dist(str1, k))


"""
77.Write a Python program to count number of non-empty substrings of
a given string.
"""


def number_of_substrings(string):
    str_len = len(string)
    return int(str_len * (str_len + 1) / 2)


print(number_of_substrings("hitanshi"))


"""
78.Write a Python program to count characters at same position in a
given string (lower and uppercase characters) as in English alphabet.
"""


def count_position(str1):
    count_chars = 0
    for i in range(len(str1)):
        if (i == ord(str1[i]) - ord("A")) or (i == ord(str1[i]) - ord("a")):
            count_chars += 1
    return count_chars


print(count_position("abchi"))


"""
79.Write a Python program to find smallest and largest word in a given string.
"""


def smallest_largest(string):
    max_length = 0
    min_length = len(string)
    list = string.split()
    for ele in list:
        if len(ele) > max_length:
            max_element = ele
            max_length = len(ele)
        if len(ele) < min_length:
            min_element = ele
            min_length = len(ele)
    print("longest_word: ", max_element)
    print("Smallest word: ", min_element)


smallest_largest("Hello How Hi")


"""
80.Write a Python program to count number of substrings with
same first and last characters of a given string.
"""


def equal_end_characters(string):
    list = string.split()
    result = 0
    for item in list:
        if item[0] == item[len(item) - 1]:
            result = result + 1
    return result


print(equal_end_characters("Hello How are you madam madam"))

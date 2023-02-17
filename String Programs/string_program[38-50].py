import string

"""
38.Write a Python program to count occurrences of a substring in a string.
"""


def count_word(string):
    count = dict()
    words = string.split()
    for i in words:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


print(count_word("Hello Mini How are you Mini"))


"""
39.Write a Python program to reverse a string..
"""


def reverse_string(string):
    return string[::-1]


print(reverse_string("Shivam"))


"""
40.Write a Python program to reverse words in a string.
"""


def reverse_words(string):
    new_words = []
    word = string.split()
    for item in word:
        new_words.append(item[::-1])
    new_string = " ".join(new_words)
    return new_string


print(reverse_words("Hello How are you"))


"""
41.Write a Python program to strip a set of characters from a string.
"""


def strip(string, chars):
    return "".join(i for i in string if i not in chars)


print("Original String: ")
print("Hello how are you")
print("After stripping e,l,o")
print(strip("Hello how are you", "elo"))

"""
42.Write a Python program to count repeated characters in a string.
"""


def count_element(str):
    dict = {}
    for ele in str:
        keys = dict.keys()
        if ele in keys:
            dict[ele] += 1
        else:
            dict[ele] = 1
    return dict


print(count_element("thequickbrownfoxjumpsoverthelazydog"))


"""
43.Write a Python program to print the square and cube symbol
in the area of a rectangle and volume of a cylinder
"""
area = 896
volume = 7854
decimals = 2
print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
decimals = 3
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))


"""
44.Write a Python program to print the index of the character in a string
"""
string1 = "Hello"
for index, char in enumerate(string1):
    print("Current character", char, "position at", index)


"""
45.Write a Python program to check if a string contains all
letters of the alphabet
"""

alphabet = set(string.ascii_lowercase)
input_string = "Hello How are you"
print(set(input_string.lower()) >= alphabet)

"""
46.Write a Python program to convert a string in a list.
"""


def convert_list(string):
    list = string.split()
    return list


print(convert_list("Hello How are you"))


"""
47.Write a Python program to lowercase first n characters in a string.
"""


def lower_case(string):
    n = 4
    new_string = ""
    for i in range(n):
        new = string[i].lower()
        new_string = new_string + new
    return new_string


print(lower_case("HITANSHI"))


"""
48.Write a Python program to swap comma and dot in a string.
"""


def swap(string):
    result = string.replace(",", "%temp%").replace(".", ",").replace("%temp%", ".")
    return result


print(swap("2.054,23"))


"""
49.Write a Python program to count and display the vowels of a given text.
"""


def count_vowels(string):
    count = 0
    list = ["a", "e", "i", "o", "u"]
    vowels = []
    for i in list:
        if i in string:
            count = count + 1
            vowels.append(i)
    print("The number of vowels are :", count)
    return vowels


print(count_vowels("Hello"))


"""
50.Write a Python program to split a string on the
last occurrence of the delimiter.
"""
str1 = "H,i,t,a,n,s,h,i"
print(str1.rsplit(",", 1))

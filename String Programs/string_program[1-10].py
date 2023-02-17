# 1.Write a Python program to calculate the length of a string.
string1 = "Hitanshi"
print("The length of the String ", string1, "is ", len(string1))


""" 2.Write a Python program to count the number of characters
(character frequency) in a string.
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


print(count_element("google.com"))


""" 3.Write a Python program to get a string made of the first 2 and
the last 2 chars from a given a string. If the string length is less than 2,
return instead of the empty string."""


def get_string(str):
    if len(str) < 2:
        print("Empty String")
    else:
        new_string = str[:2] + str[-2:]
        return new_string


print(get_string("w3resource"))

""" 4.Write a Python program to get a string from a given string
where all occurrences of its first char have been changed to '$',
except the first char itself.
 """


def change_char(str):
    char = str[0]
    str = str.replace(char, "$")
    str = char + str[1:]
    return str


print(change_char("restart"))


""" 5. Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string. """


def get_single_string(str1, str2):
    new_str1 = str2[:2] + str1[2]
    new_str2 = str1[:2] + str2[2]
    single_string = new_str1 + " " + new_str2
    return single_string


print(get_single_string("abc", "xyz"))


""" 6.Write a Python program to add 'ing' at the end of a given string
(length should be at least 3).If the given string already ends with 'ing'
then add 'ly' instead. If the string length of the given string is less than 3,
leave it unchanged."""


def add_ing(str):
    if len(str) < 3:
        return str
    elif str.endswith("ing"):
        str = str + "ly"
        return str
    else:
        str = str + "ing"
        return str


print(add_ing("abc"))
print(add_ing("string"))


""" 7.Write aPython program to find the first appearance of the substring 'not'
and 'poor' from a given string,if 'not' follows the 'poor', replace the whole
'not'...'poor' substring with 'good'. Return the resulting string."""


def replace_poor_not(str):
    fnot = str.find("not")
    fpoor = str.find("poor")

    if fnot and fpoor:
        str = str.replace(str[fnot: fpoor + 4], "good")
        return str
    else:
        return str


print(replace_poor_not("The lyrics is not that poor!"))


""" 8.Write a Python function that takes a list of words and returns the
longest word and the length of the longest one."""


def longest_word(list):
    max = 1
    for item in list:
        if len(item) > max:
            longest_item = item
            max = len(item)
    print("The longest word is: ", longest_item)
    print("The length of the longest_word is:", max)


list = ["Shreya", "Shivam", "Hitanshi", "Prish"]
longest_word(list)


# 9.Write a Python program to remove the nth index character
#  from a nonempty string.


def remove_character(string):
    if len(string) < 0:
        print("Empty String.")

    elif len(string) > 0:
        n = int(input("Enter the index you want to remove "))
        string = string.replace(string[n], "")
        return string

    else:
        print("Enter Valid index")


# print(remove_character("Hitanshi"))


"""10. Write a Python program to change a given string to a new string
where the first and last chars have been exchanged."""


def change_chars(str):
    new_str = str[-1] + str[1:-1] + str[0]
    return new_str


print(change_chars("Shivam"))

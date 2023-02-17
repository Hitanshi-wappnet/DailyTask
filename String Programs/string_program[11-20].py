""" 11. Write a Python program to remove the characters
which have odd index values of a given string."""


def remove_odd_char(str):
    new_string = ""
    for i in range(len(str)):
        if i % 2 == 0:
            new_string = new_string + str[i]
    return new_string


print(remove_odd_char("Hitanshi"))


# 12.Write a Python program to count the occurrences of each word in a given
# sentence.


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


""" 13.Write a Python script that takes input from the user and displays
 that input back in upper and lower cases."""


def upper_lower():
    string = input("Enter the string: ")
    cap = string.upper()
    small = string.lower()

    print("The String in Upper case is: ", cap)
    print("The String in Lower case is: ", small)


# upper_lower()


"""14.Write a Python program that accepts a comma separated sequence of
words as input and prints the unique words in sorted form (alphanumerically).
"""
items = "red, white, black, red, green, black"
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))


# 15.Write a Python function to create the HTML string with
# tags around the word(s).


def add_tags(string1, string2):
    result = "<" + string1 + ">" + string2 + "</" + string1 + ">"
    return result


print(add_tags("i", "Python"))
print(add_tags("b", "Python Tutorial"))


# 16. Write a Python function to insert a string in the middle of a string.


def insert_sting_middle(str, word):
    return str[:2] + word + str[2:]


print(insert_sting_middle("[[]]", "Python"))
print(insert_sting_middle("{{}}", "PHP"))
print(insert_sting_middle("<<>>", "HTML"))


""" 17.Write a Python function to get a string made of 4 copies of the
last two characters of a specified string (length must be at least 2)
"""


def get_copy(string):
    if len(string) > 2:
        new_str = string[-2:]
        print(new_str * 4)
    else:
        print("Length is too short!!")


get_copy("Python")
get_copy("Exercises")


"""
18. Write a Python function to get a string made of its first three
characters of a specified string.If the length of the string is less than 3
then return the original string.
"""


def first_three(string):
    if len(string) >= 3:
        return string[:3]
    else:
        return string


print(first_three("ipy"))
print(first_three("python"))


"""
19.Write a Python program to get the last part of a string before a
specified character
"""
str = "https://www.w3resource.com/python"
print(str.rsplit("/", 1)[0])


"""
# 20. Write a Python function to reverses a string if it's length is
# a multiple of 4.
"""


def reverse(string):
    if len(string) % 4 == 0:
        new_str = string[::-1]
        return new_str
    else:
        return string


print(reverse("Exercise"))

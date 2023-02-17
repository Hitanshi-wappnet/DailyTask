import textwrap


"""
21. Write a Python function to convert a given string to all uppercase
if it contains at least 2 uppercase characters in the first 4 characters.
"""


def convert_uppercase(string):
    count = 0
    for i in range(4):
        if string[i].isupper():
            count += 1

    if count >= 2:
        new_str = string.upper()
        return new_str
    else:
        return string


print(convert_uppercase("VidIsha"))


"""
22.Write a Python program to sort a string lexicographically.
"""


def sort(string):
    return sorted(sorted(string), key=str.upper)


print(sort("Hitanshi"))


"""
23.Write a Python program to remove a newline in Python.
"""


str1 = "\n Hello How are you \n"
string = str1.strip()
print(string)


"""
24. Write a Python program to check whether a string starts with specified
characters.
"""


string = "Hello everyone"
print(string.startswith("He"))


"""
25.Write a Python program to create a Caesar encryption.
"""


def encryption(string):
    pass


"""
26.Write a Python program to display formatted text (width=50) as output.
"""
sample_text = """
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  """
# print(textwrap.fill(sample_text, width=50))


"""
27.Write a Python program to remove existing indentation from
all of the lines in a given text.
"""
sample_text = """
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    """
text_without_Indentation = textwrap.dedent(sample_text)
# print(text_without_Indentation)


"""
28. Write a Python program to add a prefix text to all of the
lines in a string.
"""

# prefix = textwrap.indent(sample_text, '> ')
# print(prefix)


"""
29. Write a Python program to set the indentation of the first line
"""
text = textwrap.dedent(sample_text).strip()
print()
print(
    textwrap.fill(
        text,
        initial_indent="",
        subsequent_indent=" " * 4,
        width=80,
    )
)

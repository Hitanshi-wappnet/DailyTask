from itertools import product

'''
51.Write a Python program to find the first non-repeating character
in given string.
'''


def nonrepeat(string):
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i] != string[j]:
                print(string[i])
                break
        break


nonrepeat("Hello")


'''
52.Write a Python program to print all permutations with given
repetition number of characters of a given string.
'''


def permutation(string, rno):
    chars = list(string)
    results = []
    for c in product(chars, repeat=rno):
        results.append(c)
    return results


# print(permutation('abc', 3))


'''
53.Write a Python program to find the first repeated
character in a given string.
'''


def repeat(string):
    list = []
    for i in string:
        if i in list:
            return i
        else:
            list.append(i)


print(repeat("Hello"))


'''
54.Write a Python program to find the first repeated character of a given
string where the index of first occurrence is smallest.
'''


def smallest_repeat(string):
    list = []
    for i in string:
        if i in list:
            return i
        else:
            list.append(i)


print(smallest_repeat("Hello"))


'''
55.Write a Python program to find the first repeated word in a given string.
'''


def repeated_word(string):
    list1 = string.split()
    list = []
    for i in list1:
        if i in list:
            return i
        else:
            list.append(i)


print(repeated_word("Hello Mini How are you Mini"))


'''
56.Write a Python program to find the second most
repeated word in a given string.
'''


def repeated_second_word(string):
    list1 = string.split()
    list = []
    count = 0
    for i in list1:
        if i in list:
            count = count + 1
            if count == 2:
                return i
        else:
            list.append(i)


print(repeated_second_word("Hello Mini How are you Mini Hello"))


'''
57.Write a Python program to remove spaces from a given string.
'''


def remove_space(string):
    new_str = string.replace(" ", "")
    return new_str


print(remove_space("Hello How are you"))


'''
58.Write a Python program to move spaces to the front of a given string.
'''
string = "   Hello"
print(string.strip())


'''
59.Write a Python program to find the maximum occurring
character in a given string.
'''


def count_max_element(str):
    dict = {}
    for ele in str:
        keys = dict.keys()
        if ele in keys:
            dict[ele] += 1
        else:
            dict[ele] = 1
    Keymax = max(dict, key=lambda x: dict[x])
    print(Keymax)


count_max_element("Hello")


'''
60.Write a Python program to capitalize first and last
letters of each word of a given string.
'''


def capital_word(string):
    a = string.split()
    list = []
    for i in a:
        x = i[0].upper()+i[1:-1]+i[-1].upper()
        list.append(x)
    new_str = " ".join(list)
    return new_str


print(capital_word("Hello how are you"))

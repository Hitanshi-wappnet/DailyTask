#36.Write a Python program to get variable unique identification number or string.
a = 100
print(format(id(a), 'x'))
s = 'w3resource'
print(format(id(s), 'x')) 


#37. Write a Python program to find common items from two lists.
def find_common_elements(list1,list2):
    common_items=[]     #Initialize an empty array
    for i in list1:
        if i in list2:  #check the common element and append in list
            common_items.append(i)
    return common_items

list1=[1,2,3,4,5,6,7,8,80,52]
list2=[6,7,8,9,10]
print(find_common_elements(list1,list2))


#38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.
def change_position(list):
    for i in range(0, len(list), 2):
        list[i], list[i+1] = list[i+1], list[i]
        return list

print(change_position([31,45,82,65,92,30]))


#39.Write a Python program to convert a list of multiple integers into a single integer.
def convert_integer(list):
    for item in list:
        print(item,end="")     #covert multiple integers into single integer

list=[11,12,13,14]
convert_integer(list)


#40.Write a Python program to split a list based on first character of word.
from itertools import groupby
from operator import itemgetter

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)

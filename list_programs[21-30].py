import random

#21.Write a Python program to convert a list of characters into a string.
def char_to_str(list):
    string="".join(list)
    return string

print(char_to_str(["h","e","l","l","o"]))


#22.Write a Python program to find the index of an item in a specified list.
def access_index(list):
    print("The list is ",list)
    n=input("Enter the element you want to access the index from ")
    index=list.index(n)
    print("The index of ",n, "is" , index)

#access_index(["Banana","Apple","Mango","Watermelon","Orange"])


#23. Write a Python program to flatten a shallow list.
def flatten_shallow_list(list):
    new_list=[]
    for item in list:
        new_list.extend(item)
    return new_list

print(flatten_shallow_list([[1,2,3],[4,5,6],[7,8,9]]))


#24. Write a Python program to append a list to the second list.
first_list=[1,2,3,4,5,6]
second_list=[7,8,9,10]
first_list.extend(second_list)
print(first_list)


#25.Write a Python program to select an item randomly from a list.
def random_number(list):
    number=random.choice(list)
    print("The randomly selected item from ",list,"is:",number)

random_number([1,2,3,4,85,96,74])


#26.Write a python program to check whether two lists are circularly identical.
def circular_identical(list1,list2):
    temp_list=[]
    temp_list.append(list1[-1])  
    for i in range(len(list1)-1):
        temp_list.append(list1[i])
    if temp_list==list2:
        print("Both lists are circularly identical")
    else:
        print("Both the lists are not circularly identical")

list1=[10, 10, 0, 0, 10]
list2=[10, 10, 10, 0, 0]
circular_identical(list1,list2)


#27.Write a Python program to find the second smallest number in a list.
def second_smallest(list):
    list.sort()
    print("The second smallest integer is:",list[1])

second_smallest([21,52,89,63,47,15])


#28.Write a Python program to find the second largest number in a list.
def second_largest(list):
    list.sort()
    print("The second largest integer is:",list[-2])

second_largest([21,52,89,63,47,15])


#29.Write a Python program to get unique values from a list.
#Method1:
def remove_duplicates(list):
    final_list=[]
    for i in list:
        if i not in final_list:
            final_list.append(i)
    print(final_list)

remove_duplicates([1,2,3,4,1,1,3,5])

#Method2:
def remove_duplicate(list1):
    return list(set(list1))

print(remove_duplicate([1,2,2,3,4,1,1,3,5]))


#30.Write a Python program to get the frequency of the elements in a list.
def frequency_of_element(list,element):
    freq=list.count(element)
    print("The frequency of given element ",element,"is :",freq)

frequency_of_element([1,2,2,3,3,3,3,4,5,6],3)

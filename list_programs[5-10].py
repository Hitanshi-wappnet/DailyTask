'''5.Write a Python program to count the number of strings where the string length is 2 or more and 
the first and last character are same from a given list of strings.
'''
def count_string(list):
    list_count=0
    for string in list:
        if(len(string)>=2 and string[0]==string[len(string)-1] ):
            list_count = list_count + 1

    return list_count

print(count_string(['abc', 'xyz', 'aba', '1221']))


'''
6. Write a Python program to get a list, 
sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
'''

def last(n):
    return n[-1]

def get_sorted_list(list):
        return sorted(list,key=last)

print(get_sorted_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


#7.Write a Python program to remove duplicates from a list.

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


#8.Write a Python program to check a list is empty or not.
def check_empty_list(list):
    if list==[]:
        print("The list is empty")
    else:
        print("The list is not empty")

check_empty_list([1,2,3,4])

#9.Write a Python program to clone or copy a list.
def make_copy(list):
    duplicate_copy=list.copy()
    return duplicate_copy

print(make_copy([1,2,3,4,5,6]))

#10.Write a Python program to find the list of words that are longer than n from a given list of words.
def check_long(list):
    n=5
    final_list=[]
    for str in list:
        if(len(str)>n):
            final_list.append(str)   
    print("The words from ",list," list which are greater than ",n, " are",final_list)

list=["Shreya","Shivam","Maya","Ila"]
check_long(list)





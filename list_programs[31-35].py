#31.Write a Python program to count the number of elements in a list within a specified range.
def count_element(list,min,max):
    count=0
    for item in list:
        if item>min and item<max:   #Increment count in given specified range
            count += 1
    print("The number of elements between ",min ," and ", max," is ",count )

count_element([85,52,41,252,63,9,18,14,20,52],40,100)


#32. Write a Python program to check whether a list contains a sublist.
def check_sublist(list,sublist):
    count=0
    for item in range(len(list)):
        if list[item] in sublist:   #check sublist is present or not
            count += 1
            item += 1
            if list[item] not in sublist:   #If sublist is not there than break it.
                break
    
    if count==len(sublist):
        print(sublist," is present in ",list)
    else:
        print(sublist," is not present in ",list)

list=[1,2,3,4,5,6]
sublist=[2,3,4,6]
check_sublist(list,sublist)


#33.Write a Python program to generate all sublists of a list.
def get_sublist(list1):
    sub_list=[[]]      #Initialize an empty sublist
    for i in range(len(list1)+1):   
        for j in range(i+1,len(list1)+1):
            sub=list1[i:j]      #generete sublist from i to j
            sub_list.append(sub)    #append the genereted sublist into given list
    
    print(sub_list)

get_sublist([1,2,3,4])


#34.Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
pass

#35.Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
def concatenate(list):
    n=5
    new_list=[]
    for i in range(len(list)):
        for j in range(1,n):
            new_list.append(list[i]+str(j))     #concatenate given list
    return new_list

print(concatenate(["p","q"]))
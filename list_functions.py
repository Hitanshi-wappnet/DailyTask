Students=["Shivam","Shreya","Katha","Viaan","Vidhisha","Prish","Katha"]
#Rollno=[1,2,3,4,5,6]

#Append an item at the end of List
Students.append("Mukti") 

#Extend List
#Students.extend(Rollno)    

#Insert at Specific Position
Students.insert(2,"Itisha") 

#Remove Particular item in the list
Students.remove("Itisha")

#POP Particular item
Students.pop(4)  

#Clear List
#Rollno.clear()  

#Prints the index of Particular item
print(Students.index("Shivam"))

#Count the element in the list
print(Students.count("Katha"))

#Sort the element of the list in ascending order
#Students.sort()

#Reverse the list 
Students.reverse()

#Make a copy of the given list
stu=Students.copy()

print(stu)
print(Students)
#print(Rollno)

#Slicing the list:
print(Students[2:5])

'''
Write a Python program to generate and print a list of first 
and last 5 elements where the values are square of numbers between 1 and 30 (both included)

'''
def square():
    list1=[]
    for i in range(1,31):
        list1.append(i**2)
    print(list1[:5])    #Print the first Five element of the list
    print(list1[-5:])   #Print the last Five element of the list

square()


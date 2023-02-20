"""
1.Write a Python program to create a set.
"""
set1 = {1, 2, 3, 4, 5}
print(set1)     # create a set


"""
2.Write a Python program to iteration over sets.
"""
for i in set1:
    print(i, end=" ")       # Iteration of a set
print()


"""
3.Write a Python program to add member(s) in a set.
"""
set1.add(6)     # add an element in the set
print(set1)


"""
4.Write a Python program to remove item(s) from a given set.
"""
set1.remove(4)      # remove item from set
print(set1)


"""
5.Write a Python program to remove an item from a set if
 it is present in the set.
"""
print("removing 15 in set: ")
set1.discard(15)    # if item is present in list then discard it.
print(set1)
print("removing 1 in set: ")
set1.discard(1)
print(set1)


"""
6.Write a Python program to create an intersection of sets.
"""
set2 = {2, 3, 14, 15, 16}
print(set.intersection(set1, set2))     # return intersection of set


"""
7.Write a Python program to create a union of sets.
"""
print(set.union(set1, set2))    # return union of set


"""
8.Write a Python program to create set difference.
"""
print(set.difference(set1, set2))   # return difference between sets


"""
9.Write a Python program to create a symmetric difference.
"""
# return symmetric differnce between sets
print(set1.symmetric_difference(set2))


"""
10.Write a Python program to check if a set is a
subset of another set.
"""
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
# check subset is present or not in set
print("set1 is a subset of set2: ", s1.issubset(s2))
print("set2 is a subset of set1: ", s2.issubset(s1))

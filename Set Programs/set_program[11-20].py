"""
11.Write a Python program to create a shallow copy of sets.
"""
set1 = {1, 2, 3, 4}
set2 = set1.copy()  # copy elements of set
print(set2)


"""
12.Write a Python program to remove all elements from a given set.
"""
set2.clear()  # remove all elements of set
print(set2)


"""
13.Write a Python program to use of frozensets.
"""
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
# Return True if the set has no elements in common with other.
print(x.isdisjoint(y))
# Return a new set with elements in the set that are not in the others.
print(x.difference(y))
# new set with elements from both x and y
print(x | y)


"""
14.Write a Python program to find maximum and the minimum value in a set.
"""
# return maximum value from set
print("Maximum value is: ", max(set1))
# return minimum value from set
print("Minimum value is: ", min(set1))


"""
15.Write a Python program to find the length of a set.
"""
# returns length of a set
print("Length is: ", len(set1))


"""
16.Write a Python program to check
if a given value is present in a set or not.
"""
# specific value contained by set or not
print("6 is present in a set or not: ", 6 in set1)
print("4 is present in a set or not: ", 4 in set1)


"""
17.Write a Python program to check if two given
sets have no elements in common.
"""
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9}
# Return True if the set has no elements in common with other.
print(s1.isdisjoint(s2))


"""
18.Write a Python program to check if a given set is superset of itself
and superset of another given set.
"""
num1 = {1, 2, 3, 4, 5, 7}
num2 = {2, 4}
num3 = {2, 4}
print("If mum1 is superset of num2:")
print(num1 > num2)
print("Compare mum2 and num3:")
print("If mum2 is superset of num3:")
print(num2 > num3)
print("If mum3 is superset of num2:")
print(num3 > num2)


"""
19.Write a Python program to find the elements in a given set
that are not in another set.
"""
elements1 = s1.difference(s2)  # elements that are in s1 but not in s2
print(elements1)
elements2 = s2.difference(s1)  # elements that are in s1 but not in s2
print(elements2)


"""
20.Write a Python program to remove the intersection
of a 2nd set from the 1st set.
"""
s1.difference_update(s2)
print(s1)
print(s2)

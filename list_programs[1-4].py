# 1.Write a Python program to sum all the items in a list.
def list_sum(list1):
    list = list1
    sum = 0
    for i in list:
        sum = sum + i
    print("The sum of a ", list, " List is:", sum)


list_sum([5, 8, 2, 7, 9])

# 2.Write a Python program to Multiply all the items in a list.


def list_mul(list1):
    list = list1
    mul_ans = 1
    for i in list:
        mul_ans = mul_ans * i
    print("The multiplication of a ", list, " list is: ", mul_ans)


list_mul([5, 4, 2, 3])


# 3.Write a Python program to get the largest number from a list.
def get_max(list1):
    print("The maximum element from ", list1, " List is:", max(list1))


get_max([25, 31, 25, 87, 24, 56, 99, 135])


# 4.Write a Python program to get the smallest number from a list.
def get_min(list1):
    print("The minimum element from ", list1, " List is:", min(list1))


get_min([25, 31, 25, 87, 24, 56, 99, 135])

# Write a Python program to generate all sublists of a list.


def get_sublist(list1):
    sub_list = [[]]  # Initialize an empty sublist
    for i in range(len(list1) + 1):
        for j in range(i + 1, len(list1) + 1):
            sub = list1[i:j]  # generete sublist from i to j
            sub_list.append(sub)  # append the genereted sublist in list

    print(sub_list)


get_sublist([1, 2, 3, 4])

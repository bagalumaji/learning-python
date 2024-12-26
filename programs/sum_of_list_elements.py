# Program to find sum of elements in list.

def sum_of_elements(lst):
    total = 0

    for i in lst:
        total += i

    return total


print(sum_of_elements([1, 2, 3, 4, 5, 6]))

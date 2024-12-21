def add_all(*numbers):
    return sum(numbers)


def positional_args(a, *numbers):
    print("first number : ", a)
    return sum(numbers)


print("sum", add_all(1, 2, 3, 4))
print("sum", positional_args(1, 2, 3, 4))

def add():
    a = 10
    b = 20
    c = a + b
    print("addition : ", c)


def sub(a, b):
    c = a - b
    print("subtraction : ", c)


def product(a=1, b=1):
    c = a * b
    print("product : ", c)


def get_addition(a,b):
    return a + b


def future_function():
    pass


add()
sub(11, 22)
product(4)
print(get_addition(11, 11))

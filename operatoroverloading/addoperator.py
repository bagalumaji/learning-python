class Book:

    def __init__(self, price):
        self.price = price

    def __add__(self, other) -> int:
        return self.price + other.price


b1 = Book(300)
b2 = Book(500)
print(b1 + b2)

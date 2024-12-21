# constructor with default value
from classandobject.classdemo import ClassDemo


class ConstructorDemo:

    def __init__(self, roll_no=1, name="sayaji"):
        self.roll_no = roll_no
        self.name = name

    def print_data(self):
        print(f" roll no : {self.roll_no} and name : {self.name}")


obj = ConstructorDemo()
obj.print_data()

obj1 = ConstructorDemo(2, "Sharu")
obj1.print_data()

""" method in class : instance method, class method and static method"""


class MethodsInClass:
    SCHOOL_NAME = "BAGAL"

    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def print_data(self):
        print("name : ", self.name)
        print("roll no : ", self.roll_no)

    @classmethod
    def print_school_name(cls):
        print("school name : ", cls.SCHOOL_NAME)

    @staticmethod
    def hello_greeting():
        print("hello BAGAL")


obj = MethodsInClass(1, "SHARU")
obj.print_data()
obj.print_school_name()
obj.hello_greeting()

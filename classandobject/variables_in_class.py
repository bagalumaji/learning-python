""" 3 types of variables instance, class and local"""


class VariableTypes:
    # class variable
    SCHOOL_NAME = "BAGAl"

    def __init__(self):
        self.first_name = 'sayaji'
        self.last_name = 'bagal'


    def print_data(self):
        city = 'Pandharpur'
        print("first name {} and last name ".format(self.first_name,self.last_name))
        print("city : " , city)
        print("school name : ",self.SCHOOL_NAME)


obj = VariableTypes()
obj.print_data()



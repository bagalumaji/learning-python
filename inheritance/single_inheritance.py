class Abc:
    def __init__(self,a):
        print("constructor of Abc class",a)

    def demo(self):
        print("demo test from Abc")


class Xyz(Abc):
    def __init__(self, a):
        print("constructor of xyz class")
        super().__init__(a)

    def show(self):
        print("show from Xyz..")


x = Xyz(11)
x.show()
x.demo()

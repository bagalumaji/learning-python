class Outer:
    def __init__(self):
        print("outer constructor")

    class Inner:
        def __init__(self):
            print("inner constructor")

        def m1(self):
            print("m1 method")


if __name__ == "__main__":
    o = Outer()
    i = o.Inner()
    i.m1()

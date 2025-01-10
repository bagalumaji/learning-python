class P:
    def m1(self):
        print("Parent method")


class C1(P):
    def m1(self):
        print("Child-1 method")


class C2(P):
    def m1(self):
        print("Child-2 method")


class D(C1, C2):
    def m1(self):
        print("Grand Child method")


if __name__ == "__main__":
    d = D()
    d.m1()

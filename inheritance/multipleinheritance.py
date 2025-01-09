class P:
    def m1(self):
        print("parent method")


class C(P):
    def m2(self):
        print("child method")


class GC(C):
    def m3(self):
        print("grand child method")


if __name__ == "__main__":
    gc = GC()
    gc.m1()
    gc.m2()
    gc.m3()

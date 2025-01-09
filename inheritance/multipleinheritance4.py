class P1:
    def m(self):
        print("parent 1 method")


class P2:
    def m(self):
        print("parent 2 method")


class C(P1, P2):
    def m(self):
        print("child method")


if __name__ == "__main__":
    c = C()
    c.m()

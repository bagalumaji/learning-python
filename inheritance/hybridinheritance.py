class P:
    pass


class C1(P):
    pass


class C2(P):
    pass


class D(C1, C2):
    pass


if __name__ == "__main__":
    d = D()

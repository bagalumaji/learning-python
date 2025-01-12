class Demo:
    def __init__(self):
        print("object created")

    def __del__(self):
        print("destructor executed")


d1 = Demo()
d2 = Demo()
d2 = None
d3 = Demo()

print("end of program")

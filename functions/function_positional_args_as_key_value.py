def print_data(**data):
    for key, value in data.items():
        print("key : {} and value : {}".format(key, value))


print(print_data(name="sayaji", roll_no=1))

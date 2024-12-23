a = 111
b = 222
c = 333

if a > b:
    if a > c:
        print(f"largest number is : {a}")
    else:
        print(f"largest number is : {c}")
elif b > c:
    print(f"largest number is : {b}")
else:
    print(f"largest number is : {c}")

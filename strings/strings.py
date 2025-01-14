from curses.ascii import isupper

print(len("Hello python")) #12
print("Hello python".lower()) # hello python
print("Hello python".upper()) #HELLO PYTHON
print("Hello python".title()) #Hello Python
print("Hello python".capitalize()) #Hello python
print("hello python".casefold()) # hello python
print("Hello python".swapcase()) # hELLO PYTHON

print("Hello python".count("Hello")) # 1
print("Hello python".index("l")) # 2
print("hello python".find("ello"))

print("Hello python".join(["hi", "world"])) #hiHello pythonworld

print("1243".isdigit())#True
print("123ac".isalnum()) #True
print("#".isalnum()) #False
print("123".isdecimal()) #True
print("97!".isascii()) #True
print("variable_name".isidentifier()) #True
print("hello".islower()) #True
print("HELLO".isupper()) #True
print("123a".isnumeric()) #False
print("hello".isprintable()) #True


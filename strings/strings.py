print("-----------Case Conversion------------")
print(len("Hello python")) #12
print("Hello python".lower()) # hello python
print("Hello python".upper()) #HELLO PYTHON
print("Hello python".title()) #Hello Python
print("Hello python".capitalize()) #Hello python
print("hello python".casefold()) # hello python
print("Hello python".swapcase()) # hELLO PYTHON

print("--------Search and Count-------------")
print("Hello python".count("Hello")) # 1
print("Hello python".index("l")) # 2
print("hello python".find("ello"))
print("hello python".rfind("hello"))
print("hello python".rindex("python"))
print("hello python".startswith("hello"))
print("hello python".endswith("python"))


print("--------  String Modification-------------")

print("python programming".replace("o", "O")) #pythOn prOgramming
print("  abc  ".strip()) #abc
print("  abc  ".lstrip()) #"abc   "
print("  abc  ".rstrip()) #"   abc"
print("python programming".removeprefix("python")) # programming
print("python programming".removesuffix("programming")) #python

print("--------  Split and Join -------------")
print("python programming".split(" ")) #['python', 'programming']
print("python programming world".rsplit(" ", 1))#['python programming', 'world']
print("python\nprogramming".splitlines())#['python', 'programming']
print("python programming".partition(" ")) #('python', ' ', 'programming')
print("python programming".rpartition(" ")) # ('python', ' ', 'programming')
print(" ".join(["hi", "world"])) #hi world

print("--------  Character Check  -------------")

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

print("--------  Padding and Alignment  -------------")

print("Python".center(10, "-"))#--Python--
print("Python".ljust(10, "-"))#Python----
print("Python".rjust(10, "-"))#----Python
print("123".zfill(10))#0000000123

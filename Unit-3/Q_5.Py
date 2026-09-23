#string operations or methods!!!

str = "gl\tbajaj\tgroup\tof\tinstitutions\tmathura"
str1 = "hittu123"

print(str.capitalize())
print(str.casefold())
print(str.count("j"))
print(str.endswith('a'))
print(str.startswith('b'))
print(str.expandtabs(3))
print(str.find('bajaj'))
print(str.index('mathura'))
print(str.isalnum())
print(str.isdigit())
print(str.isalpha())
print(str.isidentifier())
print(str.lower())
print(str.upper())
print(str1.isnumeric())
print(str.isprintable())
print(str.isspace())



name = "Hitesh"
age = 19
marks = 7.0

print("My name is {} and i am {} years old and my marks is {}".format(name,age,marks))

print(f"Hii {name}")


text = "HII MY NAME IS HITESH CHAUHAN"

print(text.ljust(65))
print(text.rjust(55))
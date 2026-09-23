numbers = [10, 20, 30, 40, 50]

print(numbers)
print(20 in numbers)
print(20 not in numbers)
print(25 in numbers)
print(25 not in numbers)

L = [1, 2, 3, 4, 5, 6, 7]
l1 = [13,24,34]
l2 = [4,5,6]
# print(int(l1) + int(l2))

if all(l1) in L:      # this gives true if in a list there any element present 
    print("Hello")
else:
    print("Bye!!")


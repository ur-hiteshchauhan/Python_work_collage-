#WAP to create a list of value from 1 to 50 which are divisible by 2 or 4

list = [x for x in range(1, 51) if x % 2 == 0 or x % 4 == 0]

print(list)

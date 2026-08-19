num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print("Both numbers are equal. No swapping needed!")
else:
    num1, num2 = num2, num1

print(num1, num2)

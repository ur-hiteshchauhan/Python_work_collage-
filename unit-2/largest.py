num1 = int(input("enter the value of 1st number :"))
num2 = int(input("enter the vlaue of 2nd number : "))
num3 = int(input("enter the value of 3rd number : "))

if(num1>num2 & num1>num3):
    print("num1 is large")
elif(num1<num2 & num2>num3):
    print("num2 is largest")
else:
    print("num3 is largest")
    
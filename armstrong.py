num = int(input("Enter the number :"))

temp= num
sum=0

while(num>0):

    digit = num%10
    num =num//10
    sum = sum + digit**3

if sum==temp:
        print("this is armstrong number")
else:
        print("this is not a armstrong number")
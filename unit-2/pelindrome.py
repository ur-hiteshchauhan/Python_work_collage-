num = int(input("enter the number :"))
temp = num
rev =0
while(num>0):
    digit = num%10
    rev = rev*10+digit
    num = num//10

if (temp==num):
        print("this is a pelindrome number ")
else:
        print("this is not a palindrome number ")
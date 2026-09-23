import math

p = int(input("Enter the value of p :  "))
r = int(input("Enter the value of r  : "))
t = int(input("Enter the value of t : "))

SI = (p*r*t)/100

CI = (p*(1+(r/100))**t) - p

print(SI)
print(CI)

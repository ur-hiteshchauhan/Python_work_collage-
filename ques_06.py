import math

m = int(input("enter the value of m : "))
a = int(input("Ener the value of a : "))
v = int(input("Enter the value of v :"))
m1 = int(input("Enter the value of m1"))
m2 = int(input("Enter the Value of m2"))

G = 6.67*(10**(-11))
r = int(input("enter the value of radius"))

F = m*a

Kinetic_Energy = (1/2)*m*(v**2)

g = (G*m1*m2)/(r**2)

print(F)
print(Kinetic_Energy)
print(g)

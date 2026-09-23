import math 

mps = float(input("Enter speed in m/s: "))

# Converting m/s to km/h
kmph = mps * 3.6

print("Speed in km/h =", kmph)

kmph = float(input("\nEnter speed in km/h: "))

# Converting km/h to m/s
mps = kmph / 3.6

print("Speed in m/s =", mps)
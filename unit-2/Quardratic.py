import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
	if b == 0:
		print("No unique solution." if c != 0 else "Infinitely many solutions.")
	else:
		print("The solution is:", -c / b)
else:
	discriminant = b**2 - 4 * a * c
	root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
	root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
	print("The roots are:")
	print(root1)
	print(root2)

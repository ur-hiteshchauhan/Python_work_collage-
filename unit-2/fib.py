X = int(input("Enter the number of Fibonacci terms: "))

first, second = 0, 1

for _ in range(X):
	print(first, end=" ")
	first= second
	second =  first + second

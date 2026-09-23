rows = 4
columns = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")

    for j in range(columns):
        print("*", end="")

    print()

a = True
b = False

print(f"a = {a}, b = {b}\n")

# Logical OR
print("--- Logical OR (a | b) ---")
print(f"{a} | {b} = {a | b}")
print(f"{a} | {a} = {a | a}")
print(f"{b} | {b} = {b | b}")

# XOR
print("\n--- XOR (a ^ b) ---")
print(f"{a} ^ {b} = {a ^ b}")
print(f"{a} ^ {a} = {a ^ a}")
print(f"{b} ^ {b} = {b ^ b}")

# NOR (NOT of OR)
print("\n--- NOR (not (a or b)) ---")
print(f"not ({a} or {b}) = {not (a or b)}")
print(f"not ({a} or {a}) = {not (a or a)}")
print(f"not ({b} or {b}) = {not (b or b)}")

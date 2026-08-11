
num1 = 255
num2 = 546

for num in range(num1, num2 + 1):
    
    if num > 1:
        is_prime = True
        for i in range(2, num1 + 1):
            if num % i == 0:
                is_prime = False
                break  
        
        if is_prime:
            print(num, end=" ")
            
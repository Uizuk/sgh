n = int(input("Enter the range of prime numbers: "))
prime_list = []
print(f"Prime numbers between 1 and {n} are:")
for num in range(1, n + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_list.append(num) 
print(prime_list)
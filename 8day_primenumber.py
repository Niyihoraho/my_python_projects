import math

def is_prime(n):
    if n < 2:
        return f"Number is not prime: {n}"
    sqrt_n = math.sqrt(n) + 1
    for i in range(2, int(sqrt_n)):
        if n % i == 0:
            return f"Number is not prime: {n}"
    return f"Number is prime: {n}"

num = int(input("Enter the number: "))
result = is_prime(num)
print(result)

# This program checks prime numbers and prints primes up to a limit.

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


n = int(input("Enter a non-negative number: "))

if n >= 0:
    if is_prime(n):
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")
else:
    print("Please enter a non-negative number.")


limit = int(input("Enter the limit: "))

if limit >= 0:
    print("Prime numbers:", end=" ")

    for i in range(2, limit + 1):
        if is_prime(i):
            print(i, end=" ")
else:
    print("Please enter a non-negative number.")

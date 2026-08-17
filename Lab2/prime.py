# This program checks whether a number is prime
# and prints all prime numbers up to a given limit.


def is_prime(number):
    """Return True if the number is prime."""
    if number < 2:
        return False

    # Only test divisors up to the square root of the number.
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


# Check a single number
while True:
    try:
        number = int(input("Enter a positive integer: "))

        if number < 0:
            print("Please enter a non-negative integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")


# Print all prime numbers up to a limit
while True:
    try:
        limit = int(input("\nEnter the limit: "))

        if limit < 0:
            print("Please enter a non-negative integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Prime numbers up to", limit, ":")

for number in range(2, limit + 1):
    if is_prime(number):
        print(number, end=" ")

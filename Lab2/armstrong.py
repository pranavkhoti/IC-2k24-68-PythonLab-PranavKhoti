# This program checks whether a number is an Armstrong number
# and prints all Armstrong numbers within a given range.


def is_armstrong(number):
    """Return True if the number is an Armstrong number."""
    digits = len(str(number))
    temp = number
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == number


# Check a single number
while True:
    try:
        number = int(input("Enter a positive number: "))

        if number < 0:
            print("Please enter a non-negative number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")


# Print Armstrong numbers in a range
while True:
    try:
        start = int(input("\nEnter the starting value: "))
        end = int(input("Enter the ending value: "))

        if start < 0 or end < 0:
            print("Please enter non-negative values.")
        elif start > end:
            print("Starting value cannot be greater than ending value.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter integers.")

print("Armstrong numbers in the range:")

for number in range(start, end + 1):
    if is_armstrong(number):
        print(number, end=" ")

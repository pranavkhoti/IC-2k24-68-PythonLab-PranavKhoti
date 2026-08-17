# This program checks Armstrong numbers and prints Armstrong numbers in a range.

def is_armstrong(n):
    digits = len(str(n))
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n


n = int(input("Enter a non-negative number: "))

if n >= 0:
    if is_armstrong(n):
        print(n, "is an Armstrong number.")
    else:
        print(n, "is not an Armstrong number.")
else:
    print("Please enter a non-negative number.")


start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))

if start >= 0 and end >= start:
    print("Armstrong numbers:", end=" ")

    for i in range(start, end + 1):
        if is_armstrong(i):
            print(i, end=" ")
else:
    print("Invalid range.")

# This program prints Fibonacci series using a loop and recursion.

def fibonacci_recursive(n):
    global calls
    calls += 1

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Loop version
n = int(input("Enter number of terms: "))

if n > 0:
    a = 0
    b = 1

    print("Fibonacci using loop:", end=" ")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()

    # Recursive version
    calls = 0

    print("Fibonacci using recursion:", end=" ")

    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

    print()
    print("Recursive function calls:", calls)

else:
    print("Please enter a positive number.")

# This program prints three different patterns using nested loops.

n = int(input("Enter number of rows: "))

if n > 0:

    # 1. Right-angled triangle of stars
    print("\nStar Pattern:")
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

    # 2. Number pattern
    print("\nNumber Pattern:")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    # 3. Centered pyramid
    print("\nPyramid Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(i):
            print("* ", end="")
        print()

else:
    print("Please enter a positive number.")

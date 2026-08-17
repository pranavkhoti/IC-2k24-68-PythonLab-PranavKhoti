# This program checks whether a number and a string are palindromes.

# Number palindrome
n = int(input("Enter a positive number: "))

if n >= 0:
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    if original == reverse:
        print(original, "is a palindrome.")
    else:
        print(original, "is not a palindrome.")
else:
    print("Please enter a positive number.")


# String palindrome
text = input("Enter a string: ")

if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

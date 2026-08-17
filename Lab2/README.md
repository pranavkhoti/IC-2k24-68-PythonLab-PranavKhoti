# Python Lab 2

## 1. Armstrong Number

### Aim

To check whether a number is an Armstrong number and print all Armstrong numbers within a given range.

### Logic

The program calculates the number of digits and raises each digit to that power. The sum is compared with the original number. A loop is then used to find Armstrong numbers in the given range.

### Sample Input / Output

```text
Enter a non-negative number: 153
153 is an Armstrong number.
Enter starting value: 100
Enter ending value: 1000
Armstrong numbers: 153 370 371 407
```

---

## 2. Prime Number

### Aim

To check whether a number is prime and print all prime numbers up to a given limit.

### Logic

A prime number has only two factors: 1 and itself. The program checks whether the number is divisible by any number from 2 onwards and then uses a loop to find all prime numbers up to the given limit.

### Sample Input / Output

```text
Enter a non-negative number: 17
17 is a prime number.
Enter the limit: 30
Prime numbers: 2 3 5 7 11 13 17 19 23 29
```

---

## 3. Perfect Number

### Aim

To check whether a number is a perfect number and print all perfect numbers up to a given limit.

### Logic

The program finds all proper divisors of a number and adds them. If their sum is equal to the original number, it is a perfect number. A loop is used to find perfect numbers up to the given limit.

### Sample Input / Output

```text
Enter a positive number: 28
28 is a perfect number.
Enter the limit: 1000
Perfect numbers: 6 28 496
```

---

## 4. Palindrome

### Aim

To check whether a number is a palindrome using arithmetic operations and check whether a string is a palindrome.

### Logic

For the number, the digits are reversed using modulus and integer division without converting the number to a string. For the string, the reversed string is compared with the original string.

### Sample Input / Output

```text
Enter a positive number: 121
121 is a palindrome.
Enter a string: madam
The string is a palindrome.
```

---

## 5. Fibonacci Series

### Aim

To print the Fibonacci series using a loop and recursion and count the recursive function calls.

### Logic

The loop version generates each Fibonacci term using two variables. The recursive version calls itself for the previous two terms. The number of recursive function calls is counted to compare the two approaches.

### Sample Input / Output

```text
Enter number of terms: 10
Fibonacci using loop: 0 1 1 2 3 5 8 13 21 34
Fibonacci using recursion: 0 1 1 2 3 5 8 13 21 34
Recursive function calls: 177
```

---

## 6. Pattern Printing

### Aim

To print a right-angled star triangle, a number pattern and a centered pyramid using nested loops.

### Logic

Nested `for` loops are used to control the rows and columns of each pattern. Spaces are used before the stars to center the pyramid.

### Sample Input / Output

```text
Enter number of rows: 5

Star Pattern:
* 
* * 
* * * 
* * * * 
* * * * * 

Number Pattern:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

Pyramid Pattern:
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

---

## 7. Menu-Driven Application

### Aim

To combine the programs from 1 to 6 into a single menu-driven application.

### Logic

A menu displays the available operations. The user's choice determines which function is executed. The menu continues to appear until the user selects the exit option, while invalid choices are handled with an error message.

### Sample Input / Output

```text
----- MENU -----
1. Armstrong Number
2. Prime Number
3. Perfect Number
4. Palindrome
5. Fibonacci Series
6. Pattern Printing
7. Exit

Enter your choice: 2
Enter a number: 17
17 is a prime number.

Enter your choice: 7
Program ended.
```

---

## 8. Number Guessing Game

### Aim

To create a number guessing game where the user guesses a randomly generated number within a maximum of seven attempts.

### Logic

The program generates a random number between 1 and 100. After every guess, it tells the user whether the guess is too high or too low. The game ends when the number is guessed or seven attempts are used.

### Sample Input / Output

```text
Guess the number between 1 and 100.
You have 7 attempts.
Enter your guess: 50
Too low!
Enter your guess: 75
Too high!
Enter your guess: 63
Too low!
Enter your guess: 68
Correct!
You guessed it in 4 attempts.
```

---

# Analysis

## 1. For Loop vs While Loop

I preferred the `for` loop for programs such as Prime Number, Perfect Number, Fibonacci Series and Pattern Printing because the number of iterations can be controlled using a range. I preferred the `while` loop for Armstrong, Palindrome, Menu-Driven Application and Number Guessing Game where repetition depends on a condition or user input.

## 2. Fibonacci: Loop vs Recursion

The recursive version repeats more work as `n` grows because it calculates the same smaller Fibonacci values multiple times. The loop-based version calculates each term once, making it more efficient.

## 3. Prime Number: Largest Divisor to Test

The largest divisor that needs to be tested is **√n (square root of n)**. If a number has a factor greater than √n, it must have another corresponding factor smaller than √n, so checking up to √n is sufficient.

## 4. Number Guessing Game Strategy

The strategy is **Binary Search**. The user guesses the middle of the remaining range each time and eliminates half of the possible numbers after every guess. This minimizes the number of guesses needed.

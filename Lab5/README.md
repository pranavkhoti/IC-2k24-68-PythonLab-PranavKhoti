# Lab 3 - Python Programs

## Student
**Name:** Pranav Khoti

## Contents

1. ATM Simulation
2. Student Grade Calculator
3. Reverse Guessing Game
4. Guessing Game with Hints and Scoring
5. Combined Application

---

# 1. ATM Simulation

### Aim
To create a simple menu-driven ATM program for checking balance, depositing money, withdrawing money, and changing the PIN.

### Logic
The program starts with a fixed balance and PIN. After correct PIN entry, the user gets an ATM menu. Withdrawal is allowed only when the amount is not greater than the current balance.

### Sample Input / Output

**Input:**
```text
PIN: 1234
Choice: 3
Withdrawal: 6000
```

**Output:**
```text
Insufficient balance. Transaction rejected.
```

**Valid test:**
```text
Choice: 2
Deposit: 1000
```

Output:
```text
Deposit successful.
Balance: 6000
```

---

# 2. Student Grade Calculator

### Aim
To calculate the average and grade of a student using marks in five subjects.

### Logic
The program takes five marks and calculates their average. It then checks the average against the given grade ranges and stores the latest student's data.

### Sample Input / Output

**Input:**
```text
Marks: 85, 92, 78, 60, 55
```

**Output:**
```text
Average: 74.0
Grade: C
```

**Invalid test:**
```text
Enter marks: 120
```

Output:
```text
Marks must be between 0 and 100.
```

---

# 3. Reverse Guessing Game

### Aim
To make a game where the computer guesses the number selected by the user using a binary-search strategy.

### Logic
The user gives a minimum and maximum range. The computer guesses the middle number and changes the range according to the user's feedback.

### Sample Input / Output

**Input:**
```text
Minimum: 1
Maximum: 100
Secret number: 37
Feedback: H
Feedback: L
Feedback: C
```

**Output:**
```text
My guess is: 50
My guess is: 25
My guess is: 37
I found your number!
Number of guesses: 3
```

**Invalid test:**
```text
Feedback: X
```

Output:
```text
Invalid feedback. Try again.
```

---

# 4. Guessing Game with Hints and Scoring

### Aim
To create a number guessing game with hints, a scoring system, and a maximum number of attempts.

### Logic
The computer generates a random number from 1 to 100. The user starts with 100 points and loses 10 points for every wrong guess. Hints show whether the number is even or odd and whether it is a multiple of 5.

### Sample Input / Output

**Example test:**
```text
Secret number: 50
Guess: 20
```

**Output:**
```text
Too low.
Hint: The number is even.
Hint: The number is a multiple of 5.
```

After a correct guess:
```text
Correct!
You won.
Final score: 90
```

**Invalid test:**
```text
Guess: abc
```

Output:
```text
Please enter a number.
```

---

# 5. Combined Application

### Aim
To combine the ATM, Grade Calculator, and Guessing Game into one menu-driven application.

### Logic
A main menu allows the user to select one of the three programs. Each program has its own inner menu and uses `break` to return to the main menu instead of ending the complete program.

### Sample Input / Output

**Input:**
```text
Main Menu
1. ATM
2. Grade Calculator
3. Guessing Game
4. Exit

Choice: 1
```

Output:
```text
--- ATM ---
1. Check Balance
2. Deposit
3. Withdraw
4. Change PIN
5. Back to Main Menu
```

**Rejected transaction test:**
```text
Withdrawal: 7000
```

Output:
```text
Insufficient balance. Transaction rejected.
```

**Return test:**
```text
ATM Choice: 5
```

Output:
```text
===== MAIN MENU =====
```

---

# Section A and B

The answers and paper traces are provided in:

- `section_a.md`
- `section_b.md`

# Section D

The analysis answers are provided in:

- `section_d.md`

## How to Run

Open the folder in IDLE, VS Code, or another Python editor.

Run each file separately:

```text
atm.py
grade_calculator.py
reverse_guessing.py
guessing_game.py
combined_application.py
```

Python 3 is required.

## Conclusion

These programs demonstrate basic Python concepts such as variables, input/output, `if-elif-else`, `while` loops, `for` loops, random numbers, menu-driven programs, validation, and binary-search logic.

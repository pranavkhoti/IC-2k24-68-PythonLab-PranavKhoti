Python Lab - 01
By Pranav Khoti
IC-2K24-68

## 1. Variable and Identifier Practice

### Aim

To declare variables for name, age, height and student status and display their data types.

### Logic

Four variables are declared with different data types. The `type()` function is used to display the data type of each variable.

### Sample Input / Output

No input is required.

```text
Name: Pranav Type: <class 'str'>
Age: 20 Type: <class 'int'>
Height: 5.8 Type: <class 'float'>
Student: True Type: <class 'bool'>
```

---

## 2. Greeting Program

### Aim

To take the user's name, age and city as input and display them in one sentence.

### Logic

The program takes the name, age and city using `input()`. An f-string is used to combine all three values.

### Sample Input / Output

```text
Enter your name: Pranav
Enter your age: 20
Enter your city: Indore
Hello Pranav, you are 20 years old and you live in Indore.
```

---

## 3. Arithmetic Operations

### Aim

To perform basic arithmetic operations on two numbers.

### Logic

Two numbers are taken as input. The program calculates their sum, difference, product, quotient and remainder.

### Sample Input / Output

```text
Enter first number: 10
Enter second number: 3
Sum: 13.0
Difference: 7.0
Product: 30.0
Quotient: 3.3333333333333335
Remainder: 1.0
```

---

## 4. Celsius to Fahrenheit

### Aim

To convert temperature from Celsius to Fahrenheit.

### Logic

The Celsius temperature is taken as input and converted to a number. The formula `F = (C * 9/5) + 32` is used to calculate Fahrenheit.

### Sample Input / Output

```text
Enter temperature in Celsius: 25
Temperature in Fahrenheit: 77.0
```

---

## 5. String Manipulation

### Aim

To perform different operations on a full name.

### Logic

The program takes a full name as input. It converts the name to uppercase and lowercase, reverses it and calculates its length.

### Sample Input / Output

```text
Enter your full name: Pranav Khoti
Uppercase: PRANAV KHOTI
Lowercase: pranav khoti
Reversed: ito hK vanarP
Length: 12
```

---

## 6. Escape Sequence Practice

### Aim

To display a simple receipt using escape sequences.

### Logic

The `\t` escape sequence is used to align the item and price columns. The `\n` escape sequence is used to create new lines.

### Sample Input / Output

No input is required.

```text
Item            Price
-----           -----
Pen             ₹10
Notebook        ₹50
Pencil          ₹5

Total           ₹65
```

---

## 7. Menu Driven Calculator - Optional

### Aim

To create a menu-driven calculator with four arithmetic operations.

### Logic

A menu provides options for addition, subtraction, multiplication and division. The program continues running until the user selects the Exit option.

### Sample Input / Output

```text
----- Calculator -----
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter your choice: 1
Enter first number: 10
Enter second number: 5
Result: 15.0

Enter your choice: 5
Calculator closed.
```

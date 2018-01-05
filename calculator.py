"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input("> ")
    user_input = user_input.split()

    operator = user_input[0]

    if len(user_input) == 2:
        num1 = float(user_input[1])
    elif len(user_input) == 3:
        num1 = float(user_input[1])
        num2 = float(user_input[2])

    if operator == 'q':
        break
    else:
        if operator == '+':
            answer = add(num1, num2)
        elif operator == '-':
            answer = subtract(num1, num2)
        elif operator == '*':
            answer = multiply(num1, num2)
        elif operator == '/':
            answer = divide(num1, num2)
        elif operator == 'square':
            answer = square(num1)
    print answer

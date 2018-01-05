"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *
from arithmetic2 import *


# Your code goes here
# while True:
#     user_input = raw_input('> ')
#     user_input = user_input.split()

#     operator = user_input[0]

#     if len(user_input) == 2:
#         num1 = float(user_input[1])
#     elif len(user_input) == 3:
#         num1 = float(user_input[1])
#         num2 = float(user_input[2])

#     if operator == 'q':
#         break
#     else:
#         if operator == '+':
#             answer = add(num1, num2)
#         elif operator == '-':
#             answer = subtract(num1, num2)
#         elif operator == '*':
#             answer = multiply(num1, num2)
#         elif operator == '/':
#             answer = divide(num1, num2)
#         elif operator == 'square':
#             answer = square(num1)
#         elif operator == 'cube':
#             answer = cube(num1)
#         elif operator == 'power':
#             answer = power(num1, num2)
#         elif operator == '%':
#             answer = mod(num1, num2)
#     print answer

# if user inputs more than 3 things
# if user inputs non-integer for num1 and num2
# if user doesn't put spaces between inputs
# if users inputs less than 3 things for function that requires 3
# if users inputs operand that is not correct


while True:
    user_input = raw_input('> ')
    user_input = user_input.split()

    operator = user_input.pop(0)


    if operator == 'q':
        break
    else:
        if operator == '+':
            answer = add(user_input)
        elif operator == '-':
            answer = subtract(user_input)
        elif operator == '*':
            answer = multiply(user_input)
        elif operator == '/':
            answer = divide(user_input)
        elif operator == 'square':
            answer = square(user_input)
        elif operator == 'cube':
            answer = cube(user_input)
        elif operator == 'power':
            answer = power(user_input)
        elif operator == '%':
            answer = mod(user_input)
    print answer
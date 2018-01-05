"""Math functions for calculator."""


def add(list_of_numbers):
    """Return the sum of all inputs."""

    answer = 0

    for num in list_of_numbers:

        answer += float(num)

    return answer

def subtract(list_of_numbers):
    """Return all numbers subtracted from first number."""

    answer = float(list_of_numbers[0])

    for num in list_of_numbers[1:]:

        answer -= float(num)

    return answer


# def multiply(num1, num2):
#     """Multiply the two inputs together."""

#     return num1 * num2


# def divide(num1, num2):
#     """Divide the first input by the second and return the result."""

#     return float(num1) / num2


# def square(num1):
#     """Return the square of the input."""

#     # Needs only one argument

#     return num1 * num1


# def cube(num1):
#     """Return the cube of the input."""

#     # Needs only one argument

#     return num1 * num1 * num1


# def power(num1, num2):
#     """Raise num1 to the power of num and return the value."""

#     return num1 ** num2  # ** = exponent operator


# def mod(num1, num2):
#     """Return the remainder of num / num2."""

#     return num1 % num2

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


def multiply(list_of_numbers):
    """Multiply all of the inputs together."""

    answer = float(list_of_numbers[0])

    for num in list_of_numbers[1:]:

        answer *= float(num)

    return answer


def divide(list_of_numbers):
    """Divide the first input by the remaining inputs and return the result."""

    answer = float(list_of_numbers[0])

    for num in list_of_numbers[1:]:

        answer /= float(num)

    return answer


def square(list_of_numbers):
    """Return the square of the first number input."""

    # Needs only one argument
    num1 = float(list_of_numbers[0])

    return num1 * num1


def cube(list_of_numbers):
    """Return the cube of the first input."""

# Needs only one argument
    num1 = float(list_of_numbers[0])

    return num1 * num1 * num1


def power(list_of_numbers):
    """Raise num1 to the power of num2 and return the value."""

    num1 = float(list_of_numbers[0])
    num2 = float(list_of_numbers[1])

    return num1 ** num2  # ** = exponent operator


def mod(list_of_numbers):
    """Return the remainder of num / num2."""

    num1 = float(list_of_numbers[0])
    num2 = float(list_of_numbers[1])

    return num1 % num2

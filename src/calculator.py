"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

import math


def add(num1, num2):
    """Add two numbers together."""
    return num1 + num2


def subtract(num1, num2):
    """Subtract num2 from num1."""
    return num1 - num2


def multiply(num1, num2):
    """Multiply two numbers with input validation."""
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return num1 * num2


def divide(num1, num2):
    """Divide num1 by num2 with enhanced error handling."""
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if num2 == 0:
        raise ValueError("Cannot divide by zero - division by zero is undefined")
    return num1 / num2


def power(base, exponent):
    """Return base raised to the power of exponent."""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Power function requires numeric inputs")
    return math.pow(base, exponent)


def sqrt(number):
    """Return the square root of a number."""
    if number < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(number)


if __name__ == "__main__":
    # Example usage
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")

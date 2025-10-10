"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""

import sys
import click
from .calculator import add, subtract, multiply, divide



@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""
    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Format result: integer if possible, otherwise 2 decimals
        if result == int(result):
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")

    except ValueError as err:
        click.echo(f"Error: {err}")
        sys.exit(1)
    except TypeError as err:
        click.echo(f"Error: {err}")
        sys.exit(1)


if __name__ == "__main__":
    # Use Click's CLI invocation correctly
    calculate()  # no arguments passed manually; click handles argv

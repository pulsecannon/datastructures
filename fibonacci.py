"""Defines algorithm to compute fibonacci numbers."""

def fibonacci_recursive(number):
    """Recursive fibonacci number generator."""
    if number <= 1:
        return 1
    else:
        return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)

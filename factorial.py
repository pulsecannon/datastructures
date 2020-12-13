"""Defines code to compute factorial of a number."""


def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#!/usr/bin/python3
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """This function returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """This function returns the product of two numbers."""
    return a * b

def divide(a, b):
    """This function returns the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

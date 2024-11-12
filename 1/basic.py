# Basic Arithmetic Operators
def arithmetic_operations(a, b):
    print("Arithmetic Operations:")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")
    print(f"Floor Division: {a} // {b} = {a // b}\n")

# Assignment Operators
def assignment_operations():
    print("Assignment Operations:")
    x = 10
    print(f"x = 10 -> x = {x}")
    x += 5
    print(f"x += 5 -> x = {x}")
    x -= 3
    print(f"x -= 3 -> x = {x}")
    x *= 2
    print(f"x *= 2 -> x = {x}")
    x /= 4
    print(f"x /= 4 -> x = {x}")
    x %= 3
    print(f"x %= 3 -> x = {x}")
    x **= 2
    print(f"x **= 2 -> x = {x}")
    x //= 2
    print(f"x //= 2 -> x = {x}\n")

# Comparison Operators
def comparison_operations(a, b):
    print("Comparison Operations:")
    print(f"{a} == {b} -> {a == b}")
    print(f"{a} != {b} -> {a != b}")
    print(f"{a} > {b} -> {a > b}")
    print(f"{a} < {b} -> {a < b}")
    print(f"{a} >= {b} -> {a >= b}")
    print(f"{a} <= {b} -> {a <= b}\n")

# Test the functions
a = 15
b = 4
arithmetic_operations(a, b)
assignment_operations()
comparison_operations(a, b)

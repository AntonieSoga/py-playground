"""
Python Variables and Assignment
Description: A guide to variable declaration, dynamic typing, 
type casting, and multi-variable initialization.
"""

# Variables act as symbolic names that reference data objects in memory.
# In Python, declaration happens automatically upon assignment.
x = 5         # Assigns an integer object to name 'x'
y = 'String'  # Assigns a string object to name 'y'

print(f"Integer variable: {x}")
print(f"String variable: {y}")

# --- Dynamic Typing ---
# Variables are not bound to a specific data type and can be reassigned 
# to objects of different types during execution.
x = 4        # x is initially an int
x = "Sally"  # x is reassigned to a str; the previous int is garbage collected
print(f"Reassigned x: {x}")

# --- Type Casting ---
# Casting is used when you need to ensure a variable holds a specific type.
# This is common when handling user input or performing math on strings.
x = str(3)    # Forces 'x' to be the string '3'
y = int(3)    # Forces 'y' to be the integer 3
z = float(3)  # Forces 'z' to be the float 3.0

print(f"Casted values: {x} (str), {y} (int), {z} (float)")

# --- Multi-Variable Assignment (Unpacking) ---
# You can assign multiple distinct values to multiple variables in a single line.
# Note: The number of variables must match the number of values.
x, y, z = "Orange", "Banana", "Cherry"
print(f"Multiple assignment: {x}, {y}, {z}")

# --- Shared Value Assignment ---
# Multiple variables can point to the exact same object in memory.
x = y = z = "Orange"
print(f"Shared assignment: {x}, {y}, {z}")
"""
Python Data Types Overview
Description: A reference script demonstrating the initialization and 
classification of built-in Python data types.
"""

# 01 Text Type -> str
# Strings are immutable sequences of Unicode characters.
print("01 Text Data Type (str):", "Hello Python", type("Hello Python"))

# 02 Numeric Types -> int, float, complex
# int: Arbitrary precision integers.
# float: Double-precision floating point numbers.
# complex: Numbers with a real and imaginary part (denoted by 'j').
print("02 Numeric (int):", 42, type(42))
print("02 Numeric (float):", 3.14159, type(3.14159))
print("02 Numeric (complex):", 1 + 2j, type(1 + 2j))

# 03 Sequence Types -> list, tuple, range
# list: Mutable, ordered sequence of items.
# tuple: Immutable, ordered sequence; often used for fixed data.
# range: An efficient immutable sequence of numbers, usually used in loops.
print("03 Sequence (list):", [1, 2, 3, 'apple'], type([1, 2, 3, 'apple']))
print("03 Sequence (tuple):", (10, 20, 'orange'), type((10, 20, 'orange')))
print("03 Sequence (range):", range(5), type(range(5)))

# 04 Mapping Type -> dict
# Dictionaries store data in key-value pairs. 
# Keys must be immutable (hashable) types like strings, numbers, or tuples.
print("04 Mapping (dict):", {"id": 1, "name": "Antonie"}, type({"id": 1}))

# 05 Set Types -> set, frozenset
# set: Unordered collection of unique items; mutable.
# frozenset: An immutable version of a set; can be used as a dictionary key.
print("05 Set (set):", {1, 2, 3, 3}, type({1, 2, 3}))
print("05 Set (frozenset):", frozenset({1, 2, 3}), type(frozenset({1, 2, 3})))

# 06 Boolean Type -> bool
# Represents logical values: True or False.
print("06 Boolean (bool):", True, type(True))

# 07 Binary Types -> bytes, bytearray, memoryview
# bytes: Immutable sequences of single bytes.
# bytearray: Mutable version of bytes.
# memoryview: Allows access to the internal data of an object without copying.
print("07 Binary (bytes):", b"Hello", type(b"Hello"))
print("07 Binary (bytearray):", bytearray(5), type(bytearray(5)))
print("07 Binary (memoryview):", memoryview(b"ABC"), type(memoryview(b"ABC")))

# 08 None Type -> NoneType
# Represents the absence of a value or a null pointer.
print("08 None Type:", None, type(None))
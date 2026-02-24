"""
Module 1.3 - Data Types
Understanding different types of data

Python has several built-in data types. The most common are:
- str (string): Text
- int (integer): Whole numbers
- float: Decimal numbers
- bool (boolean): True or False
"""

# ============================================================================
# CONCEPT: String (str)
# ============================================================================
# Strings are text. Use single or double quotes.

greeting = "Hello"
name = 'Python'
sentence = "I'm learning Python!"  # Can mix quotes

print(greeting)
print(name)
print(sentence)

# String methods (things you can do with strings)
text = "python"
print(text.upper())  # PYTHON
print(text.capitalize())  # Python
print(len(text))  # Length: 6

# ============================================================================
# CONCEPT: Integer (int)
# ============================================================================
# Integers are whole numbers (positive, negative, or zero)

count = 42
negative = -10
zero = 0

print(count)
print(negative + 5)  # -5
print(zero)

# ============================================================================
# CONCEPT: Float
# ============================================================================
# Floats are decimal numbers

pi = 3.14159
temperature = -273.15
price = 19.99

print(pi)
print(round(pi, 2))  # Round to 2 decimal places: 3.14
print(int(pi))  # Convert to integer: 3

# ============================================================================
# CONCEPT: Boolean (bool)
# ============================================================================
# Booleans are True or False

is_active = True
is_empty = False

print(is_active)
print(not is_active)  # not True = False
print(not is_empty)   # not False = True

# ============================================================================
# CONCEPT: Checking data types
# ============================================================================
# Use the type() function to see what type a variable is

age = 25
print(type(age))  # <class 'int'>

price = 19.99
print(type(price))  # <class 'float'>

name = "Alice"
print(type(name))  # <class 'str'>

is_online = True
print(type(is_online))  # <class 'bool'>

# ============================================================================
# CONCEPT: Converting between types
# ============================================================================
# You can convert one type to another using str(), int(), float(), bool()

# String to integer
age_text = "30"
age_number = int(age_text)
print(age_number + 5)  # 35

# Integer to string
number = 42
text = str(number)
print(text + " is the answer")  # "42 is the answer"

# Float to integer
price = 19.99
price_int = int(price)  # 19 (loses the decimal)
print(price_int)

# Any type to boolean
print(bool(1))  # True
print(bool(0))  # False
print(bool("hello"))  # True
print(bool(""))  # False (empty string is False)

# ============================================================================
# CONCEPT: Type errors
# ============================================================================
# If you try to do something that doesn't make sense for a type, Python errors

# Uncomment the lines below to see the errors:
# print("5" + 5)  # Error: can't add string and int
# print(int("hello"))  # Error: "hello" can't be converted to int

# Fix: Convert to the same type first
print("5" + str(5))  # "55"
print(int("5") + 5)  # 10

# ============================================================================
# YOUR TURN: Practice
# ============================================================================
# 1. Create a string variable with a sentence
# 2. Create an integer variable with your age
# 3. Create a float variable with your height
# 4. Create a boolean variable with whether you like Python
# 5. Print the type of each variable


# ============================================================================
# KEY TAKEAWAY
# ============================================================================
# - Python has different data types: str, int, float, bool
# - Use type() to check a variable's type
# - Use str(), int(), float(), bool() to convert between types
# - Some operations only work with certain types
# - Mixing types (like "5" + 5) causes errors
#
# Next: Learn about operators and calculations

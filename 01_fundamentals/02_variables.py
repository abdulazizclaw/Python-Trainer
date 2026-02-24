"""
Module 1.2 - Variables
Storing and using data

A variable is a container that holds a value. Think of it like a labeled box
where you can store information and use it later.
"""

# ============================================================================
# CONCEPT: Creating variables
# ============================================================================
# Syntax: variable_name = value
# The = sign means "assign" (put a value into a variable)

# Example 1: String variables (text)
name = "Alice"
city = "New York"

print("Name:", name)
print("City:", city)

# Example 2: Integer variables (whole numbers)
age = 25
year = 2024

print("Age:", age)
print("Year:", year)

# Example 3: Float variables (decimal numbers)
height = 5.7
temperature = 98.6

print("Height:", height)
print("Temperature:", temperature)

# Example 4: Boolean variables (True or False)
is_student = True
is_retired = False

print("Is student:", is_student)
print("Is retired:", is_retired)

# ============================================================================
# CONCEPT: Naming variables
# ============================================================================
# Rules for variable names:
# - Must start with a letter or underscore (_)
# - Can contain letters, numbers, and underscores
# - No spaces allowed
# - Python is case-sensitive (name != Name != NAME)
# - Avoid Python keywords (like print, if, for, etc.)
# - Use descriptive names!

# Good variable names:
student_name = "Bob"
user_email = "bob@example.com"
total_price = 49.99

# Avoid these:
x = "bad name - too vague"
a = 10  # also vague
name123 = "better but still not great"

# ============================================================================
# CONCEPT: Changing variable values
# ============================================================================
# You can reassign a variable to a new value

score = 10
print("Score:", score)

score = 15  # Update the value
print("Score after update:", score)

# ============================================================================
# CONCEPT: Using variables together
# ============================================================================
# You can combine variables in calculations and strings

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Combine strings with +

print("Full name:", full_name)

# Numbers can be combined mathematically
hours_worked = 8
hourly_rate = 15
daily_pay = hours_worked * hourly_rate

print("Daily pay:", daily_pay)

# ============================================================================
# YOUR TURN: Practice
# ============================================================================
# Create a variable for:
# 1. Your favorite color
# 2. Your age
# 3. Your height

# Then print them out


# ============================================================================
# KEY TAKEAWAY
# ============================================================================
# - Variables store values (text, numbers, true/false)
# - Use = to assign a value to a variable
# - Use descriptive names
# - Variables can be reused and changed
# - Variables can be combined with + (strings) or math operations (numbers)
#
# Next: Learn about data types and how to convert between them

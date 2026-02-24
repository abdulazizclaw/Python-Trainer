"""
Project 1: Age Calculator - Solution

This is the complete working solution.
Study this code to understand how it works.
"""

# ============================================================================
# STEP 1: Get user input
# ============================================================================
birth_year_input = input("What year were you born? ")
current_year_input = input("What is the current year? ")

# ============================================================================
# STEP 2: Convert to integers
# ============================================================================
birth_year = int(birth_year_input)
current_year = int(current_year_input)

# ============================================================================
# STEP 3: Calculate ages
# ============================================================================
age = current_year - birth_year
age_next_year = age + 1
age_five_years_ago = age - 5
age_in_months = age * 12

# ============================================================================
# STEP 4: Display results
# ============================================================================
print("\n" + "=" * 32)
print("Welcome to the Age Calculator!")
print("=" * 32)
print(f"Birth year: {birth_year}")
print(f"Current year: {current_year}")
print("=" * 32)
print(f"Your current age: {age} years old")
print(f"Next year you'll be: {age_next_year} years old")
print(f"5 years ago you were: {age_five_years_ago} years old")
print(f"You're approximately {age_in_months} months old!")
print("=" * 32 + "\n")

# ============================================================================
# EXPLANATION
# ============================================================================
# Line 1-2: input() asks the user a question and stores their answer as a string
# Line 5-6: int() converts the string input to an integer so we can do math
# Line 10-13: Calculate different ages using arithmetic
# Line 17+: print() displays the results to the user
#
# Note: We used f-strings (f"text {variable}") to insert variables into strings.
# This is a clean way to format output.

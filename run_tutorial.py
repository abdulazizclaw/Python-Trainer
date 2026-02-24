#!/usr/bin/env python3
"""
Python Trainer - Interactive Learning Platform

This is a guided, interactive Python learning platform for complete beginners.
Each lesson teaches one concept at a time with explanations and guided practice.
"""

import os
import time
from pathlib import Path

# Colors for terminal output
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'
CYAN = '\033[96m'

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header(text):
    """Print formatted header"""
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}{text.center(60)}{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}\n")

def print_lesson(title):
    """Print lesson title"""
    print(f"\n{BOLD}{CYAN}▶ {title}{RESET}")
    print(f"{CYAN}{'-'*60}{RESET}\n")

def print_concept(concept_name):
    """Print concept heading"""
    print(f"\n{BOLD}{GREEN}📌 {concept_name}{RESET}")
    print(f"{GREEN}{'-'*40}{RESET}\n")

def print_code(code_snippet, description=""):
    """Print code with formatting"""
    if description:
        print(f"{YELLOW}{description}{RESET}\n")
    print(f"{BOLD}>>> {code_snippet}{RESET}\n")

def print_output(output):
    """Print code output"""
    print(f"{CYAN}Output:{RESET}")
    print(f"{output}\n")

def pause():
    """Wait for user to continue"""
    input(f"{BOLD}Press Enter to continue...{RESET}")

def input_check(prompt, expected=None):
    """Get user input with optional validation"""
    while True:
        user_input = input(f"{BOLD}{YELLOW}{prompt}{RESET} ").strip()
        if expected is None:
            return user_input
        if user_input.lower() == expected.lower():
            print(f"{GREEN}✓ Correct!{RESET}\n")
            return user_input
        else:
            print(f"{RED}✗ Not quite. Try again.{RESET}\n")

# ============================================================================
# LESSON 1.1: HELLO WORLD
# ============================================================================

def lesson_1_1_hello_world():
    """Interactive Hello World lesson"""
    clear_screen()
    print_lesson("Lesson 1.1: Your First Program - Hello World!")
    
    print("Welcome to Python Trainer! 🎉\n")
    print("In this lesson, you'll write your very first Python program.")
    print("Don't worry - we'll do it together, step by step.\n")
    pause()
    
    print_concept("What is Python?")
    print("Python is a programming language - a way to give instructions to a computer.")
    print("Python is great for beginners because it reads almost like English!\n")
    pause()
    
    print_concept("The print() function")
    print("The print() function is Python's way of displaying text on your screen.")
    print("Think of it as 'telling Python: display this message to the user'\n")
    
    print_code('print("Hello, World!")', "Here's the simplest program:")
    print_output("Hello, World!")
    
    print("Let's break this down:")
    print("  • print( ) = This is the command to display text")
    print("  • \"Hello, World!\" = This is the text we want to display")
    print("  • The quotes tell Python 'this is text, not a command'\n")
    pause()
    
    print_concept("Your turn!")
    print("Now YOU try it. Type this exact line into a text editor:\n")
    print(f"{BOLD}print(\"I'm learning Python!\"){RESET}\n")
    print("Then save the file as 'hello.py' and run it.\n")
    
    input_check("Did you see your message appear? (yes/no)", "yes")
    print(f"{GREEN}Excellent! You just wrote your first program!{RESET}\n")
    pause()
    
    print_concept("Key Takeaway")
    print("  ✓ print() displays text on the screen")
    print("  ✓ Text must be wrapped in quotes: \"like this\"")
    print("  ✓ Python reads top to bottom, one line at a time\n")
    print("Ready for the next lesson? Let's learn about VARIABLES!\n")
    pause()

# ============================================================================
# LESSON 1.2: VARIABLES
# ============================================================================

def lesson_1_2_variables():
    """Interactive Variables lesson"""
    clear_screen()
    print_lesson("Lesson 1.2: Variables - Storing Information")
    
    print("In the last lesson, we printed text directly.")
    print("But what if we want to SAVE and REUSE text? That's where VARIABLES come in.\n")
    pause()
    
    print_concept("What is a Variable?")
    print("A variable is like a labeled box where you store information.")
    print("Later, you can open that box and use what's inside.\n")
    print("Think of it like naming a container:\n")
    print("  📦 box_name = \"what's inside\"\n")
    pause()
    
    print_concept("Creating a Variable")
    print("To create a variable, use this pattern:\n")
    print(f"{BOLD}variable_name = value{RESET}\n")
    print("The = sign means 'store this value in this box'\n")
    
    print_code('name = "Alice"', "Example:")
    print("This creates a box called 'name' and puts 'Alice' inside it.\n")
    pause()
    
    print_concept("Using a Variable")
    print("Once you've stored something in a variable, you can use it:\n")
    print_code('print(name)', "This code:")
    print_output("Alice")
    print("Python looked inside the 'name' box and printed what it found!\n")
    pause()
    
    print_concept("Why Use Variables?")
    print("You can reuse the same information multiple times:\n")
    print_code('name = "Bob"\nprint(name)\nprint(name)\nprint(name)', "Code:")
    print_output("Bob\nBob\nBob")
    print("We typed 'Bob' once, but printed it three times!\n")
    pause()
    
    print_concept("Naming Variables")
    print("Rules for variable names:")
    print("  ✓ Can have letters, numbers, and underscores: my_name_1")
    print("  ✓ Must start with a letter or underscore")
    print("  ✗ Can't have spaces: my name (NO)")
    print("  ✗ Can't use Python keywords: print, if, for (NO)\n")
    print("Use names that make sense! 'age' is better than 'x'\n")
    pause()
    
    print_concept("Your Turn!")
    print("Create a variable with your favorite food:\n")
    print(f"{BOLD}favorite_food = \"pizza\"{RESET}\n")
    print("Then print it:\n")
    print(f"{BOLD}print(favorite_food){RESET}\n")
    input_check("Did you create and print your variable? (yes/no)", "yes")
    print(f"{GREEN}Perfect! You've mastered variables!{RESET}\n")
    pause()
    
    print_concept("Key Takeaway")
    print("  ✓ Variables store information for later use")
    print("  ✓ Create with: variable_name = value")
    print("  ✓ Use the variable name whenever you need that value")
    print("  ✓ Pick variable names that make sense\n")
    print("Next: Let's learn about different TYPES of data!\n")
    pause()

# ============================================================================
# LESSON 1.3: DATA TYPES
# ============================================================================

def lesson_1_3_data_types():
    """Interactive Data Types lesson"""
    clear_screen()
    print_lesson("Lesson 1.3: Data Types - Different Kinds of Information")
    
    print("Variables can store different TYPES of information.")
    print("Python needs to know what type of data you're storing.\n")
    pause()
    
    print_concept("The Four Main Data Types")
    print("1. STRING (text) - Words and sentences in quotes")
    print("2. INTEGER (numbers) - Whole numbers like 5, 100, -3")
    print("3. FLOAT (decimals) - Numbers with decimals like 3.14")
    print("4. BOOLEAN (true/false) - Only True or False\n")
    pause()
    
    print_concept("1. STRINGS - Text")
    print("Strings are text wrapped in quotes (single or double):\n")
    print_code('name = "Alice"', "Example:")
    print_code('city = \'New York\'', "Both work:")
    print("Pick one style and stick with it for consistency.\n")
    pause()
    
    print_concept("2. INTEGERS - Whole Numbers")
    print("Integers are numbers WITHOUT decimals:\n")
    print_code('age = 25', "Example:")
    print_code('temperature = -5', "Can be negative:")
    print("Notice: NO quotes around the numbers!\n")
    pause()
    
    print_concept("3. FLOATS - Decimal Numbers")
    print("Floats have a decimal point:\n")
    print_code('height = 5.7', "Example:")
    print_code('pi = 3.14159', "Can have many decimals:")
    print("Floats let you store measurements and precise values.\n")
    pause()
    
    print_concept("4. BOOLEANS - True or False")
    print("Booleans are used for yes/no questions:\n")
    print_code('is_student = True', "Example:")
    print_code('is_retired = False', "Only two values:")
    print("Note: True and False have NO quotes - they're special!\n")
    pause()
    
    print_concept("How to Check the Type")
    print("Python has a type() function to check what type something is:\n")
    print_code('print(type(25))', "Example:")
    print_output("<class 'int'>")
    print_code('print(type("hello"))', "Another example:")
    print_output("<class 'str'>")
    print("This tells you the data type!\n")
    pause()
    
    print_concept("Your Turn!")
    print("Create these variables and check their types:\n")
    print(f"{BOLD}name = \"Your Name\"{RESET}")
    print(f"{BOLD}age = 20{RESET}")
    print(f"{BOLD}height = 5.9{RESET}")
    print(f"{BOLD}is_cool = True{RESET}\n")
    print("Then use print(type(...)) on each one.\n")
    input_check("Did you create all four types of data? (yes/no)", "yes")
    print(f"{GREEN}Awesome! You understand data types!{RESET}\n")
    pause()
    
    print_concept("Key Takeaway")
    print("  ✓ Strings: \"text\" (with quotes)")
    print("  ✓ Integers: 42 (whole numbers, no quotes)")
    print("  ✓ Floats: 3.14 (decimals, no quotes)")
    print("  ✓ Booleans: True or False (no quotes)")
    print("  ✓ Use type() to check what type something is\n")
    print("Next: Let's build your FIRST PROJECT!\n")
    pause()

# ============================================================================
# PROJECT 1: AGE CALCULATOR - GUIDED BUILD
# ============================================================================

def project_1_age_calculator():
    """Interactive Age Calculator project"""
    clear_screen()
    print_lesson("Project 1: Age Calculator")
    
    print("Now you're ready to build your first REAL program!")
    print("You'll create a calculator that figures out someone's age.\n")
    print("We'll build it step by step together.\n")
    pause()
    
    print_concept("Project Requirements")
    print("Your program will:")
    print("  1. Ask the user: 'What year were you born?'")
    print("  2. Ask the user: 'What is the current year?'")
    print("  3. Calculate their age (current year - birth year)")
    print("  4. Display the result\n")
    pause()
    
    print_concept("Step 1: Get Input from the User")
    print("We need to ASK the user for information.")
    print("We use the input() function:\n")
    print_code('birth_year = input(\"What year were you born? \")', "Example:")
    print("This asks the user a question and saves their answer.\n")
    pause()
    
    print_concept("IMPORTANT: input() returns a STRING")
    print("When you ask the user a question, they type text.")
    print("Even if they type '1990', Python treats it as \"1990\" (text).\n")
    print("We need to convert it to a number to do math!\n")
    print_code('birth_year = int(input(\"What year were you born? \"))', "Solution:")
    print("The int() function converts \"1990\" to 1990 (a number)\n")
    pause()
    
    print_concept("Step 2: Do the Calculation")
    print("Now we have the birth year (as a number), we can do math:\n")
    print_code('age = current_year - birth_year', "Calculate age:")
    print("Simple subtraction!\n")
    pause()
    
    print_concept("Step 3: Display the Result")
    print("Finally, show the result to the user:\n")
    print_code('print(f\"Your age is {age} years old\")', "Use an f-string:")
    print("The f before the quote lets us put variables inside {brackets}\n")
    pause()
    
    print_concept("The Complete Program")
    print("Here's the full program:\n")
    complete_code = '''birth_year = int(input("What year were you born? "))
current_year = int(input("What is the current year? "))
age = current_year - birth_year
print(f"Your age is {age} years old")'''
    print(f"{BOLD}{complete_code}{RESET}\n")
    pause()
    
    print_concept("Now BUILD IT!")
    print("Open a text editor and type this program exactly.")
    print("Save it as 'age_calculator.py'")
    print("Run it and test it with your own birth year!\n")
    input_check("Did you create and run the age calculator? (yes/no)", "yes")
    print(f"{GREEN}AMAZING! You just built a real program!{RESET}\n")
    pause()
    
    print_concept("What You Learned")
    print("  ✓ How to get input from the user")
    print("  ✓ How to convert text to numbers (int())")
    print("  ✓ How to do math with variables")
    print("  ✓ How to display results with f-strings\n")
    print("YOU ARE NOW A PROGRAMMER! 🎉\n")
    pause()

# ============================================================================
# MAIN MENU
# ============================================================================

def show_main_menu():
    """Display main menu"""
    clear_screen()
    print_header("PYTHON TRAINER - Learn Python from Zero to Hero")
    
    print(f"{BOLD}Choose a lesson:{RESET}\n")
    print(f"1. {BOLD}Module 1: Fundamentals{RESET}")
    print("   1.1 - Hello World")
    print("   1.2 - Variables")
    print("   1.3 - Data Types")
    print("   1.4 - Project: Age Calculator\n")
    
    print(f"2. {BOLD}Module 2: Control Flow{RESET} (Coming soon)")
    print(f"3. {BOLD}Module 3: Data Structures{RESET} (Coming soon)")
    print(f"4. {BOLD}Module 4: File I/O{RESET} (Coming soon)")
    print(f"5. {BOLD}Module 5: Object-Oriented Programming{RESET} (Coming soon)\n")
    
    print(f"6. {BOLD}Exit{RESET}\n")

def main():
    """Main trainer loop"""
    while True:
        show_main_menu()
        choice = input(f"{BOLD}{YELLOW}Enter your choice (1-6): {RESET}").strip()
        
        if choice == '1':
            # Module 1 submenu
            while True:
                clear_screen()
                print(f"{BOLD}{CYAN}Module 1: Fundamentals{RESET}\n")
                print("1. Lesson 1.1 - Hello World")
                print("2. Lesson 1.2 - Variables")
                print("3. Lesson 1.3 - Data Types")
                print("4. Project 1 - Age Calculator")
                print("5. Back to main menu\n")
                
                sub_choice = input(f"{BOLD}{YELLOW}Enter your choice (1-5): {RESET}").strip()
                
                if sub_choice == '1':
                    lesson_1_1_hello_world()
                elif sub_choice == '2':
                    lesson_1_2_variables()
                elif sub_choice == '3':
                    lesson_1_3_data_types()
                elif sub_choice == '4':
                    project_1_age_calculator()
                elif sub_choice == '5':
                    break
                else:
                    print(f"{RED}Invalid choice. Try again.{RESET}")
                    input(f"{BOLD}Press Enter to continue...{RESET}")
        
        elif choice == '6':
            clear_screen()
            print_header("Thanks for learning Python!")
            print(f"{GREEN}Keep coding! You're on your way to becoming a programmer! 🚀{RESET}\n")
            break
        
        else:
            print(f"{RED}Invalid choice. Try again.{RESET}")
            input(f"{BOLD}Press Enter to continue...{RESET}")

if __name__ == '__main__':
    main()

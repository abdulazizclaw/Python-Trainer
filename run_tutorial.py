#!/usr/bin/env python3
"""
Python Trainer - Tutorial Runner

This script helps you navigate through the Python training modules.
It displays lessons and guides you through projects.
"""

import os
import subprocess
from pathlib import Path

# Colors for terminal output
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_header(text):
    """Print a formatted header"""
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}{text.center(60)}{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}\n")

def print_section(text):
    """Print a formatted section"""
    print(f"\n{BOLD}{GREEN}{text}{RESET}")
    print(f"{GREEN}{'-'*len(text)}{RESET}\n")

def run_file(filepath):
    """Run a Python file"""
    filepath = str(filepath)  # Convert Path to string
    try:
        subprocess.run(['python3', filepath], check=True)
    except subprocess.CalledProcessError:
        print(f"{RED}Error running {filepath}{RESET}")
    except FileNotFoundError:
        print(f"{RED}File not found: {filepath}{RESET}")

def show_menu():
    """Display the main menu"""
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
    
    print(f"6. {BOLD}Run Tests{RESET}")
    print(f"7. {BOLD}Exit{RESET}\n")

def main():
    """Main tutorial runner"""
    # Get the directory where this script is located
    script_path = Path(__file__).resolve()
    base_path = script_path.parent
    
    while True:
        show_menu()
        choice = input(f"{BOLD}Enter your choice (1-7): {RESET}").strip()
        
        if choice == '1':
            # Module 1 submenu
            while True:
                print_section("Module 1: Fundamentals")
                print("1. Hello World (01_hello_world.py)")
                print("2. Variables (02_variables.py)")
                print("3. Data Types (03_data_types.py)")
                print("4. Project: Age Calculator")
                print("5. Back to main menu\n")
                
                sub_choice = input(f"{BOLD}Enter your choice (1-5): {RESET}").strip()
                
                if sub_choice == '1':
                    run_file(base_path / '01_fundamentals' / '01_hello_world.py')
                elif sub_choice == '2':
                    run_file(base_path / '01_fundamentals' / '02_variables.py')
                elif sub_choice == '3':
                    run_file(base_path / '01_fundamentals' / '03_data_types.py')
                elif sub_choice == '4':
                    print_section("Project 1: Age Calculator")
                    print(f"{YELLOW}Ready to build your first project?{RESET}\n")
                    print("Option 1: Start with starter_code.py (recommended)")
                    print("Option 2: View solution.py")
                    print("Option 3: Run solution.py\n")
                    
                    proj_choice = input(f"{BOLD}Enter your choice (1-3): {RESET}").strip()
                    if proj_choice == '1':
                        run_file(base_path / '01_fundamentals' / 'project_1_age_calculator' / 'starter_code.py')
                    elif proj_choice == '2':
                        with open(base_path / '01_fundamentals' / 'project_1_age_calculator' / 'solution.py') as f:
                            print(f.read())
                    elif proj_choice == '3':
                        run_file(base_path / '01_fundamentals' / 'project_1_age_calculator' / 'solution.py')
                elif sub_choice == '5':
                    break
        
        elif choice == '6':
            print_section("Running Tests")
            print(f"{YELLOW}Test suite coming soon!{RESET}\n")
        
        elif choice == '7':
            print_header("Thanks for learning Python!")
            print(f"{GREEN}Keep coding! 🚀{RESET}\n")
            break
        
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")

if __name__ == '__main__':
    main()

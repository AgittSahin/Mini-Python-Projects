import os

print("""
 _____________________
|  _________________  |
| |                 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
\n""")
def addition(f_num, s_num):
    return f_num + s_num

def subtraction(f_num, s_num):
    return f_num - s_num

def multiplication(f_num, s_num):
    return f_num * s_num

def division(f_num, s_num):
    if s_num != 0:
        return f_num / s_num
    else:
        return "Error: Division by zero is not allowed"

def modulus(f_num, s_num):
    return f_num % s_num

def Exponentiation(f_num, s_num):
    return f_num ** s_num

operations = {"+": addition, "-": subtraction, "*": multiplication, "/": division, "%": modulus, "**": Exponentiation}
first_number = int(input("What is your first number: "))
continue_calculation = True

def calculation():
    print(f"Operations: {list(operations.keys())}")
    operation = input(f"Which operation do you want to use: ")
    second_number = int(input("What is your next number: "))
    global result
    result = (operations[operation](first_number, second_number))
    calculation_printer = print(f"{first_number} {operation} {second_number} = {result}")
    if operation in operations:
        calculation_printer
        global cont_calc
        cont_calc = input(f"Type 'yes' to continue calculating with {result}, 'new' to start a new calculation, or type 'quit' to quit the Calculator \n").lower()
    
calculation()

while continue_calculation:
    if cont_calc == "new":
        os.system('cls' if os.name == 'nt' else 'clear')
        first_number = int(input("What is your first number: "))
        calculation()
    elif cont_calc == "yes":
        first_number = result
        calculation()
    elif cont_calc == "quit":
        os.system('cls' if os.name == 'nt' else 'clear')
        continue_calculation = False
        break
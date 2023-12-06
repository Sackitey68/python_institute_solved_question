import os

def addition(a, b):
    result = a + b
    return result


def multiplication(a, b):
    result = a * b
    return result


def division(a, b):
    result = a / b
    return result


def subtraction(a, b):
    result = a - b
    return result


def calculator():
    num1 = int(input("Enter first number: "))
    print("+\n-\n*\n/\n")

    continue_program = True
    while continue_program:
        operator = input("Pick an operation: ")
        num2 = int(input("Enter next number: "))

        if operator == "+":
            output = addition(num1, num2)
            print(f"{num1} + {num2} = {output}")

        elif operator == "*":
            output = multiplication(num1, num2)
            print(f"{num1} * {num2} = {output}")

        elif operator == "/":
            output = division(num1, num2)
            print(f"{num1} / {num2} = {output}")

        elif operator == "-":
            output = subtraction(num1, num2)
            print(f"{num1} - {num2} = {output}")

        else:
            print("Invalid operator")

        play_again = input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit ").lower()
        if play_again == 'y':
            num1 = output

        elif play_again == 'n':
            continue_program = False
            os.system('cls')
            calculator()

        else:
            continue_program = False
            print("Bye")


calculator()

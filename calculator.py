def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

while True:
    try:
        print(" ----------------------------------------")
        operation = input("Choose an operation (add, subtract, multiply, divide): ")
        print("")
        if operation not in ["add", "subtract", "multiply", "divide"]:
            raise ValueError("Invalid operation!")
        print(" ----------------------------------------")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(" ----------------------------------------")
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        else:
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed!")
            result = divide(num1, num2)

        print("Result:", result)

    except ValueError as ve:
        print("Invalid input:", ve)
    except ZeroDivisionError as zde:
        print("Error:", zde)

    try_again = input("Do you want to try again? (yes/no): ")
    if try_again.lower() != "yes":
        break

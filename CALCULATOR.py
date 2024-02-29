def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return x / y

def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation in operations:
        result = operations[operation](num1, num2)

        if result is not None:
            print(f"Result: {result}")
        else:
            print("Error: Invalid operation.")
    else:
        print("Error: Invalid operation.")

if __name__ == "__main__":
    while True:
        print("\nWelcome to the simple calculator!")
        print("Enter 'q' to quit.")

        choice = input("Enter operation (+, -, *, /): ")

        if choice == 'q':
            break
        else:
            calculator()
x = int(input("Enter a number: "))
def add():
    y = int(input("Enter another number: "))
    print(x + y)

def subtract():
    y = int(input("Enter another number: "))
    print(x - y)

def multiply():
    y = int(input("Enter another number: "))
    print(x * y)

def divide():
    y = int(input("Enter another number: "))
    print(x / y)

def main():
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = int(input("Enter your choice: "))
    if operation == 1:
        add()
    elif operation == 2:
        subtract()
    elif operation == 3:
        multiply()
    elif operation == 4:
        divide()
    else:
        print("Invalid choice")

main()
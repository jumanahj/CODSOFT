def main():
    while True:
        # Display a menu of operations
        print("\nSimple Calculator")
        print("Available operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        # Prompt user to choose an operation
        operation = input("Choose an operation (+, -, *, /) or 'exit' to quit: ")

        # Check if the user wants to exit
        if operation.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        # Prompt user to input the first number
        num1 = float(input("Enter the first number: "))
        
        # Prompt user to input the second number
        num2 = float(input("Enter the second number: "))
        
        # Perform the calculation based on the chosen operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            # Check for division by zero
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Invalid operation. Please choose +, -, *, / or 'exit'.")
            continue
        
        # Display the result
        print(f"The result of {num1} {operation} {num2} is: {result}")

if __name__ == "__main__":
    main()

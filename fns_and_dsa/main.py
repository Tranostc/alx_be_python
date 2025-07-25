# main.py

from arithmetic_operations import perform_operation

def main():
    # Input numbers
    num1 = 5
    num2 = 6
    
    # Example operations
    operations = ['add', 'subtract', 'multiply', 'divide']
    
    for operation in operations:
        result = perform_operation(num1, num2, operation)
        print(f"{operation.capitalize()} of {num1} and {num2}: {result}")

if __name__ == "__main__":
    main()
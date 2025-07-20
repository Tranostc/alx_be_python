def draw_pattern():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))
    
    # Ensure the input is a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        return
    
    # Initialize row counter
    row = 0
    
    # Use a while loop to iterate through each row
    while row < size:
        # Use a for loop to print asterisks for each column
        for col in range(size):
            print("*", end="")
        # Print a newline character after each row
        print()
        # Increment the row counter
        row += 1

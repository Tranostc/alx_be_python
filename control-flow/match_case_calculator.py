num1 = 10
num2 =5 
print(f"First number: {num1}, Second number: {num2}")
operation = input("Enter the operation you want to perform (+, -, *, /): ").strip()

match operation:
	case "+":
		Result = num1 + num2
	case "-":
		Result = num1 - num2
	case "*":
		Result = num1 * num2
	case "/":
		if num2 != 0:
			Result = num1 / num2
		else:
			print("Error: Can not divide by zero.")
			Result = None
	case _:
		Result = None

if Result is not None:
	print(f"Result: {Result}")

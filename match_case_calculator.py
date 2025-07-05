num1 = int(input("Enter the first number: "))
print()
num2 = int(input("Enter the second number: "))
print()
operation = input("Enter operation (+, -, /, *): ").strip()
if operation == "+":
    result = num1 + num2
    print(f" the result is {result}")
elif operation == "-":
    result = num1 - num2
    print(f" the result is {result}")
elif operation == "*":
    result = num1 * num2
    print(f" the result is {result}")
elif operation == "/":
    
    if num2 == 0:
        print("Error: division by zero is not allowed.")
    else:
        result = num1 / num2
    print(f" the result is {result}")
def calculator():
    
    print("Welcome to the simple calculator")
    # get user input for the number and operation
    num1 = float(input("Enter your first number:"))
    num2 = float(input("Enter your second number:"))
    operation = input("Enter the operation (+,-,*,/,//,%): ")
    
    # perform the calculation basedon the operation
    if operation == '+':
        result = num1 + num2 
        operation_name = "Addition"
    elif operation == '-':
        result = num1 -num2
        operation_name = "Subtraction"
    elif operation == '*':
        result = num1 * num2 
        operation_name = "Multiplication"
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is undefined. ")
            return 
        result =  num1 / num2
        operation_name = "Division" 
    elif operation == '//':
        result = num1 // num2
        operation_name ="Integer Division"
    elif operation == '%':
        result = num1 % num2
        operation_name = "Modulus" 
    else:
        print("Invalid operation ! Enter one of these (+,-,*,/,//,%)")
        return 

    # print the result in readable format
    print(f"/n{operation_name}:")
    print(f"{num1} {operation} {num2} = {result}")
# Run the calculator
calculator()             


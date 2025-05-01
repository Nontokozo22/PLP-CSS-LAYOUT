
def calculator():
    firstNum = int(input("Enter first number: "))
    secondNum= int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        result = firstNum + secondNum
    elif operation == '-':
        result = firstNum - secondNum
    elif operation == '*':
        result = firstNum * secondNum
    elif operation == '/':
        if secondNum != 0:
            result = firstNum/ secondNum
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")
        return

    print(f"{firstNum} {operation} {secondNum} = {result}")

calculator()





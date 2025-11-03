def calculator(x,y,operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y 
    elif operation == '*':
        return (x * y)
    elif operation == '/':
        return x / y
    else:
        return("Go fuck yourself")
    
if __name__ == '__main__':
    x = float(input("enter first number: "))
    operation = input('enter the operation: ')
    y = float(input("enter second number: "))
    print(calculator(x,y,operation))


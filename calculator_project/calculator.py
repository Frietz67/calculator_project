def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error"
    return a / b

def power(base, exp):
    return base ** exp

def sqrt(a):
    if a < 0:
        return "Error"
    return a ** 0.5

def percentage(total, percent):
    return (total * percent) / 100

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error"
    return a / b

def power(base, exp):
    return base ** exp

def sqrt(a):
    if a < 0:
        return "Error"
    return a ** 0.5

def percentage(total, percent):
    return (total * percent) / 100

if __name__ == "__main__":
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")

    choice = input("Enter choice (1-7): ")

    if choice in ['1', '2', '3', '4', '5', '7']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", sub(num1, num2))
        elif choice == '3':
            print("Result:", mul(num1, num2))
        elif choice == '4':
            print("Result:", div(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
        elif choice == '7':
            print("Result:", percentage(num1, num2))

    elif choice == '6':
        num = float(input("Enter number: "))
        print("Result:", sqrt(num))
        
    else:
        print("Invalid Input")
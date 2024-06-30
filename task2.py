print("----------CALCULATOR------------------")
print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 3 for divide")
print("Press 0 for exit")
while 1:
    ch = input("Enter your choice:")
    if ch == '1':
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print(num1 + num2)
    elif ch == '2':
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print(num1 - num2)
    elif ch == '3':
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print(num1 * num2)
    elif ch == '4':
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print(num1 / num2)
    elif ch == '0':
        break
    else:
        print("Invalid choice")

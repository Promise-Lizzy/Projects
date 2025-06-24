#Control Statements

num = -5

if num > 0:
    print("The number is positive.")
elif num == 0:
    print("This number is Zero.")
else:
    print("The number is negative.")
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num1} is less than {num2}.")
else:
    print("Both numbers are equal.")
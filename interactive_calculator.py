number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

condition = input("What calculation do you want to perform (+, -, *, /, %): ")

if condition == '+':
    print(f"Your sum result is: {number1 + number2}")

elif condition == '-':
    print(f"Your subtraction result is: {number1 - number2}")

elif condition == '*':
    print(f"Your multiplication result is: {number1 * number2}")

elif condition == '/':
    if number2 != 0:
        print(f"Your division result is: {number1 / number2}")
    else:
        print("Cannot divide by zero!")

elif condition == '%':
    if number2 != 0:
        print(f"Your modulus result is: {number1 % number2}")
    else:
        print("Cannot perform modulus by zero!")

else:
    print("Invalid operator!")
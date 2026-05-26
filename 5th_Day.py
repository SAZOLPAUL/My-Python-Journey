
  ## if statement
age = 20
if age >= 18:
    print("You are allowed to vote in the elections.")

## else statement
age = 16
if age >= 18:
    print("You are allowed to vote in the elections.")
else:
    print("You are not allowed to vote in the elections!")

## elif statement
age = 20
if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
else:
    print("You are an adult")

## nested conditional statement
num = int(input("Enter the number: "))

if num > 0:
    print("The number is positive")

    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")

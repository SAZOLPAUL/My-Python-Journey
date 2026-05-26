##if statement
age=20
if age>=18:
  print("you are allowed to vote in the elections")

##else statement
age=16
if age>=18:
  print("you are allowed to vote in the elections.")
else:
  print("you are not allowed to vote in the elections!")

##elif statement
age=20
if age<13:
  print("you are a child")
elif age<18:
  print("you are a teenager")
else:
  print("you are a adult")
  
  
##nested conditional statement
num=int(input("enter the number: "))
if num>0:
  print("the number is positive")
  if num%2==0:
    print("the number is even")
  else:
    print("the number is odd")
else:
  print("the number is zero or nagative")

  
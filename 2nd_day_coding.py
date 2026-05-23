##this is a single line comments

"""this is a 
multiline comments"""

##basic syntax rulea in python 
##case sensitivity- python is case sensitivity
name="sazol"
Name="paul"
print(name)
print(Name)

##indentation
##python uses indentation to define blocks of code.Consistent use of space (commonly 4) or a tab is required
age=25
if age>20:
  print(age)
print(age)

##line contination
total=1+2+3+4+5+6+7+\
4+6+7
print(total)

##multiple statement on a singal line
x=2;y=3;z=x+y
print(z)

##variable assigment 
age=55
name="sazol"
num=23.12
print(type(age))
print(type(name))
print(type(num))

##type inference
variable=10
print(type(variable))
variable="sazol"
print(type(variable))

##code examples of indentation
if True:
  print("correct indentation")
  if False:
    print("this is not print")
  print("this will print") 
print("outside of the print")
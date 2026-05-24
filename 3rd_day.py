##declaring and assigning variable
age=19
height=5.8
name="sazol"
is_student=True
print("age : ",age)
print("height : ",height)
print("name : ",name)

##naming convertions
##valid variable name
fast_name="sazol"
last_name="paul"

##invalid variable name
#5age=30
#fast-name="sazol"
#@name="sazol"

##variable types
age=19#int
height=5.8#float
name="sazol"#str
is_student=True#bool
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

##type convert
age="30"
print(type(int(age)))
height=5.11
print(type(int(height)))
print(type(str(height)))

##dynamic typing
var=10
print(var,type(var))

var="hello"
print(var,type(var))

var=3.14
print(var,type(var))

##input
age=int(input("Enter your age : "))
print(age,type(age))

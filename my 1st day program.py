print("hello world")
a="sazol paul"
b="from kanandia"
c=19
print(f"{a} {b} and my age is {c}")
d=input("enter your father name:")
print(f"your father name is {d}")
ages=[25, 35 ,55, 75, 86, 40]
highest_age=ages[0]
for age in ages:
  if age>highest_age:
    highest_age=age
print(f"highest age is {highest_age}")
lowest_age=ages[0]
for age in ages:
  if age<lowest_age:
    lowest_age=age
print(f"lowest age is {lowest_age}")  



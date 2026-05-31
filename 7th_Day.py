lis=[]
print(type(lis))

names=["SAZOL","PAUL",1,2,3,4,5]
print(names)

mixed_list=[1,"hello",1,23,True]
print(mixed_list)

##acessing list element
fruits=["apple","banana","charry","kiwi","gauva"]
print(fruits[0])
print(fruits[2])
print(fruits[4])
print(fruits[-1])
print(fruits[1:4])

##modifying the list element
fruits[1]="watermelon"
print(fruits)

##list methods
fruits.append("orange")
print(fruits)

fruits.insert(1,"pum")
print(fruits)

fruits.remove("pum")
print(fruits)

##remove and return the last 
popped_fruits=fruits.pop()
print(popped_fruits)
print(fruits)

index=fruits.index("charry")
print(index)

fruits.insert(2,"banana")
print(fruits.count("banana"))
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

fruits.clear()
print(fruits)
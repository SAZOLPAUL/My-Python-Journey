##creating dictionaries
empty_dict={}
print(type(empty_dict))

empty_dict=dict()
print(type(empty_dict))

student={"name":"sazol","age":19,"grade":40}
print(student)
print(type(student))

##singal key is always used
student={"name":"sazol","age":19,"name":"sujoy"}
print(student)

##accessing dictionaries elements
student={"name":"sazol","age":19,"grade":"A"}
print(student['grade'])
print(student["name"])

##accessing using get() methode
print(student.get('name'))
print(student.get('last_name'))
print(student.get('last_name','Not Available'))

##modifying dictionaries element
#dictionaries are mutable, so we can add, update or delete the element
print(student)
student['age']=20
student['address']="Bangladesh"
print(student)

del student['grade']
print(student)

##dictionary methode
keys=student.keys()
print(keys)
values=student.values()
print(values)
items=student.items()
print(items)

##shallow copy
student_copy=student
print(student_copy)
print(student)

student['name']="sazol2"
print(student)
print(student_copy)

student_copy1=student.copy()

student['name']='sazol3'
print(student)
print(student_copy1)

##iterating over dictionary 
##you can use loops to iterate over dictionaries, keys,values or items

#iterating over keys 
for keys in student.keys():
  print(keys)
  
#iterating over values
for values in student.values():
  print(values)

##iterate over key value pairs
for key,value in student.items():
  print(key,":",value)

##nested dictionaries
students={
  "student1":{'name':"sazol","age":19,"grade":"A"},
  
  "student2":{"name":"sujoy","age":6,"address":"Bangladesh"},
  
  "student3":{"name":"puza","age":11,"grade":"B"}
}
print(students)


##access nested dictionariy
print(students["student2"]["name"])

print(students["student3"]["grade"])

##iterate over nested dictionaries

for student_id,student_info in students.items():
  
  print(f"{student_id} : {student_info}")
  
  for key,value in student_info.items():
    
    print(f'{key} : {value}')
    
##dictionarie compherehention
squares={x:x**2 for x in range(5)}
print(squares)

##condition dictionarie compherehention
even={x:x**2 for x in range(11) if x%2==0}
print(even)

##practical example

#use a dictionarie to contn the frequency of the element i list

numbers=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
frequency={}
for number in numbers:
  if number in frequency:
    frequency[number]+=1
  else:
    frequency[number]=1
print(frequency)    
  
##merge 2 dictionaries into one 
dict1={'a':1,'b':2}
dict2={'b':3,'d':4}
merged_dict={**dict1,**dict2}
print(merged_dict)

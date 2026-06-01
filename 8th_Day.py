##slicing list
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[1:5])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::-2])

##
for number in numbers:
  print(number)
  
##iterating with index
for index,number in enumerate(numbers):
  print(index,number)
  
##list comprehension
list=[]
for x in range(1,11):
  list.append(x**2)
print(list)  

list=[x**2 for x in range(1,15)]
print(list)

##list comprehension
#basic list comprehension
sqaure=[num**2 for num in range(1,11)]
print(sqaure)

##list comprehension with condition
lst=[]
for i in range(10):
  if i%2==0:
    lst.append(i)

print(lst)

even_number=[num for num in range(10) if num%2==0]
print(even_number)

##nested list comprehension
list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
pair=[[i,j] for i in list1 for j in list2]
print(pair)

##list comprehension with function calls 
words=["hello","world","my","name","is","sazol"]
lengths=[len(word) for word in words]
print(lengths)
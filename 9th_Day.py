##creating a tuple
empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))

lst=list()
print(type(lst))
tpl=tuple()
print(type(tpl))

number=tuple([1,2,3,4,5,6,7,8])
print(number,type(number))

mixed_tuple=(1,"hello world",3.14,True)
print(mixed_tuple)

##accessing tuple element
numbers=(1,2,3,4,5,6,7,8,9)
print(numbers[2])
print(numbers[5])
print(numbers[-1])
print(numbers[:5])
print(numbers[:7])
print(numbers[3:8])
print(numbers[4:])
print(numbers[::-1])

##tuple operation
concatenation_tuple=numbers + mixed_tuple
print(concatenation_tuple)

print(mixed_tuple*4)
print(numbers*4)
 
##immutable nature of tuples
lst=[1,2,3,4,5,6]
print(lst)
lst[1]="sazol"
print(lst)


##tuples methods
print(numbers.count(1))
print(numbers.index(4))

##packing and unpacking tuples
#packing
packed_tuple=1,"hello world",3.141
print(packed_tuple)

#unpacking a tuple
a,b,c=packed_tuple
print(a)
print(b)
print(c)

#unpacking with *
numbers=1,2,3,4,5,6,7
first,*middle,last=numbers
print(first)
print(middle)
print(last)

##nested list
lst=[[1,2,3,4,5],[6,7,8,9,10],[1,"hello world",3.141]]
print(lst[0][1])
print(lst[1][1:3])
print(lst[2][::-1])
print(lst)

##access the tuple inside a tuple 
nested_tuple=((1,2,3),("a","b","c"),(True,False))
print(nested_tuple[0])
print(nested_tuple[1][2])

##iterating over nested tuples
for sub_tuple in nested_tuple:
  for item in sub_tuple:
    print(item,end=" ")
  print()  
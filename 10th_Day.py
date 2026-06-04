##create sets
my_set={1,2,3,4,5}
print(my_set)
print(type(my_set))

my_empty_set=set()
print(type(my_empty_set))

my_set=set([1,2,3,4,5,6,7,8])
print(my_set,type(my_set))

my_set={1,1,2,2,3,3,4,4,4,5,5,5,5,5,5}
print(my_set)

##BASICS SET OPERATION
#adding element
my_set.add(6)
print(my_set)
my_set.add(6)
print(my_set)

##remove the element from a SET
my_set.remove(5)
print(my_set)

my_set={1,2,3,4,5,6,7,8}
my_set.discard(4)
print(my_set)

my_set={1,2,3,4,5,6,7,8}
my_set.discard(33)
print(my_set)

##pop classmethod
remove_element=my_set.pop()
print(remove_element)
print(my_set)

##clear all the element
my_set.clear()
print(my_set)


##set membership test
my_set={1,2,3,4,5,6,7,8}
print(3 in my_set)
print(10 in my_set)

##mathematical OPERATION
set1={1,2,3,4,5,6,7,8}
set2={4,5,6,7,8,9,10}

#union
union_set=set1.union(set2)
print(union_set)

#intersection
intersection_set=set1.intersection(set2)
print(intersection_set)

set1.intersection_update(set2)
print(set1)

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

#difference
set1.difference_update(set2)
print(set1)

#another way
set1={1,2,3,4,5,6}
result=set2.difference(set1)
print(result)

##symmetric difference
set1.symmetric_difference_update(set2)
print(set1)

set1={1,2,3,4,5,6}
ruselt=set2.symmetric_difference(set1)
print(ruselt)

##set methodes
set1={1,2,3,4,5}
set2={3,4,5}

#is subset
print(set1.issubset(set2))

#is superset
print(set1.issuperset(set2))

##counting unique word in text
text="In this class i am discussing about sets"
words=text.split()

#convert list of word to set to get unique words

unique_words=set(words)
print(unique_words)
print(len(unique_words))
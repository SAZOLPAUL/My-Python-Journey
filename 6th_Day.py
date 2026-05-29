##for loop
for i in range(5):
  print(i)
  
for i in range(1,6):
  print(i)
  
for i in range(1,11,2):
  print(i)
  
for i in range(10,1,-2):
  print(i)

#strings
stri="sazol paul"
for i in stri:
  print(i)
  
##while loop
count=0
while count<5:
  print(count)
  count=count + 1
  
##loop control statements
#break
for i in range(10):
  if i==5:
    break
  print(i)

#continue
for i in range(10):
  if i%2==0:
    continue
  print(i)
  
#pass
for i in range(10):
  if i==3:
    pass
  print(i)
  
  
##nested loops
for i in range(3):
  for j in range(2):
    print(f"i:{i} and j:{j}")
    
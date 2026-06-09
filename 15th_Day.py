#===================================================
#EXCEPTION HANDLING WITH TRY, EXCEPT AND BLOCK
#===================================================

#----------------------------
#TRY, EXCEPT AND BLOCK
#----------------------------

#----------------------------
#NameError
#----------------------------

try:
  a = b
except:
 print("the variable isn't assigned")
 
#----------------------------
#NameError 
#----------------------------

try:
  a = b 
except NameError as ex:
  print(ex)

#----------------------------
#ZeroDivisionError
#----------------------------

try:
  print(1/0)
except ZeroDivisionError as ex:
  print(ex)
  print("Plece enter the denominator greater than ZERO")

  

try:
  result=1/2
  a=b 
except ZeroDivisionError as ex:
  print(ex)
  print("Please enter the denominator greater than ZERO")
except Exception as ex1:
  print(ex1)
  print("Main exception got caught here")
  

try:
  num=int(input("Enter a number: "))
  result=10/num 
except ValueError:
  print("This is not a valid number")
except ZeroDivisionError:
  print("enter denominator greater than  ZERO")
except Exception as ex:
  print(ex)
else:
  print(f"the result is {result}")
finally:
  print("Execution complete.")

#----------------------------  
#FileNotFoundError  
#----------------------------  
try:
    file = open("example1.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("File not found")
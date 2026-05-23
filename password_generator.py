import random
print("wellcome to password generator!")
lett="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY"
num="1234567890"
sym="!@#$%^&*"
all_chars=lett + num + sym 
length=int(input("How long do you want your password to be? (e.g., 8, 12):"))
password=""
for i in range (length):
  random_char=random.choice(all_chars)
  password=password + random_char
print(f"your password is: {password}")
  
  
#====================================
# OOPS CONCEPTS
#====================================

#-----------------------------
# classes and object
#-----------------------------

# a class is a blueprint for creating objects

class Car:
    pass

audi = Car()
bmw = Car()

print(type(audi))
print(type(bmw))

print(audi)
print(bmw)

audi.windows = 4
print(audi.windows)

tata = Car()
tata.doors = 4
print(tata.doors)

print(dir(tata))

#---------------------------------------
# instance variable and method
#---------------------------------------

class Dog:

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

# create object
dog1 = Dog('Toshi', 3)
print(dog1)
print(dog1.name)
print(dog1.age)

dog2 = Dog('Tom', 4)
print(dog2)
print(dog2.name)
print(dog2.age)

#---------------------------------------------
# define a class with instance method
#---------------------------------------------

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof")

dog1 = Dog("buddy", 3)
dog1.bark()

dog2 = Dog("lucy", 4)
dog2.bark()

#=======================================
# modeling a bank account
#=======================================

#---------------------------------------------
# define a class for bank account
#---------------------------------------------

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} is deposited. New balance is {self.balance}")

    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient funds!")

        else:
            self.balance -= amount
            print(f"{amount} is withdrawn. New balance is {self.balance}")

    def get_balance(self):
        return self.balance

#---------------------------------------------
# create an account
#---------------------------------------------

account = BankAccount("sazol", 5000)
print(account.balance)

#-----------------------------
# call instance method
#-----------------------------

account.deposit(400)
print(account.balance)

account.withdraw(500)
print(account.balance)

print(account.get_balance())
#====================================
# Inheritance
#====================================

#------------------------------------
# Parent Class
#------------------------------------

class Car:

    def __init__(self, windows, doors, engine_type):
        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type

    def drive(self):
        print(f"The person will drive the {self.engine_type} car.")


# Create Object

car1 = Car(4, 5, "Petrol")

car1.drive()

print(car1)

#------------------------------------
# Child Class
#------------------------------------

class Tesla(Car):

    def __init__(self, windows, doors, engine_type, is_self_driving):

        super().__init__(windows, doors, engine_type)

        self.is_self_driving = is_self_driving

    def self_driving(self):
        print(f"Tesla supports self driving: {self.is_self_driving}")


# Create Object

tesla1 = Tesla(4, 3, "Electric", True)

tesla1.self_driving()

tesla1.drive()

print(tesla1)

#====================================
# Multiple Inheritance
#====================================

#------------------------------------
# Parent Class 1
#------------------------------------

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Subclass must implement this method")


#------------------------------------
# Parent Class 2
#------------------------------------

class Pet:

    def __init__(self, owner):
        self.owner = owner


#------------------------------------
# Child Class
#------------------------------------

class Dog(Animal, Pet):

    def __init__(self, name, owner):

        Animal.__init__(self, name)

        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} says Woof!"


# Create Object

dog = Dog("Buddy", "Sazol")

print(dog.speak())

print(f"Owner: {dog.owner}")
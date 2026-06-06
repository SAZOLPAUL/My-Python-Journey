# ==========================
# Lambda Function
# ==========================

# Normal Function
def addition(a, b):
    return a + b

print(addition(1, 2))

# Lambda Function
addition = lambda a, b: a + b

print(type(addition))
print(addition(3, 4))


# ==========================
# Even Number Check
# ==========================

def even(a):
    if a % 2 == 0:
        return f"{a} is an even number"
    else:
        return f"{a} isn't an even number"

print(even(7))

# Lambda Version
even1 = lambda a: a % 2 == 0

print(even1(4))


# ==========================
# Addition of Three Numbers
# ==========================

def addition_three(x, y, z):
    return x + y + z

print(addition_three(3, 4, 6))

addition_three = lambda x, y, z: x + y + z

print(addition_three(3, 4, 6))


# ==========================
# map()
# ==========================

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def square(number):
    return number ** 2

print(square(4))

# Using Lambda with map
squares = list(map(lambda num: num ** 2, numbers))
print(squares)

# Using Function with map
squares = list(map(square, numbers))
print(squares)


# ==========================
# Multiple Iterables with map()
# ==========================

num1 = [1, 2, 3, 4]
num2 = [5, 6, 7, 8]

added_numbers = list(map(lambda x, y: x + y, num1, num2))
print(added_numbers)


# ==========================
# Convert Strings to Integers
# ==========================

str_num = ['1', '2', '3', '4', '5', '6']

int_num = list(map(int, str_num))
print(int_num)


# ==========================
# Convert Words to Uppercase
# ==========================

words = ['apple', 'banana', 'cherry']

upper_words = list(map(str.upper, words))
print(upper_words)


# ==========================
# Extract Names from Dictionary
# ==========================

def get_name(person):
    return person['name']

people = [
    {"name": "sazol", "age": 19},
    {"name": "sujoy", "age": 6}
]

print(list(map(get_name, people)))


# ==========================
# filter()
# ==========================

def even(num):
    return num % 2 == 0

print(even(24))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter(even, lst)))


# ==========================
# filter() with Lambda
# ==========================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)


# ==========================
# Multiple Conditions in filter()
# ==========================

even_and_greater_than_five = list(
    filter(lambda x: x > 5 and x % 2 == 0, numbers)
)

print(even_and_greater_than_five)


# ==========================
# Filter Dictionaries
# ==========================

people = [
    {"name": "sazol", "age": 19},
    {"name": "jon", "age": 33},
    {"name": "jonathon", "age": 36}
]

def age_greater_than_25(person):
    return person['age'] > 25

print(list(filter(age_greater_than_25, people)))
#question one
#python --version

import math

#question 2

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

#question 3
print('Almando')
print('Hafenaaje')
print('Namibia')
print('I am enjoying 30 days of python')

#Question 4

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Eveline', 'Python','Namibia']))
print(type('Almando'))
print(type('Hafenaaje'))
print(type('Namibia'))

#exercise 3
#Q1
# 1. Number Types
integer_number = 10      # Integer
float_number = 3.14      # Float
complex_number = 2 + 3j  # Complex Number

# 2. String
name = "Python Programming"  # String

# 3. Boolean
is_python_fun = True  # Boolean

# 4. List (Ordered, Mutable)
fruits = ["apple", "banana", "cherry", 34]

# 5. Tuple (Ordered, Immutable)
coordinates = (10.5, 20.3, 5.7)

# 6. Set (Unordered, Unique Elements)
unique_numbers = {1, 2, 3, 4, 5, 5}  # Output: {1, 2, 3, 4, 5}

# 7. Dictionary (Key-Value Pairs)
person = {
    "name": "Almando",
    "age": 25,
    "city": "Windhoek"
}

# Printing all values
print(integer_number, float_number, complex_number)
print(name)
print(is_python_fun)
print(fruits)
print(coordinates)
print(unique_numbers)
print(person)

#q2
# given points
x1, y1 = 2, 3
x2, y2 = 10, 8

# Calculate euclidean distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Print the result
print("Euclidean Distance:", distance)
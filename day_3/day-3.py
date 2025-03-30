#Exercise - day 3
age = 25
height = 1.75
complex_number = 3 + 4j

# Prompt user for base and height of the triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))

# Calculate the area of the triangle
area = 0.5 * base * height

# Display the result
print(f"The area of the triangle is {area}")

# Prompt user for the sides of the triangle
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))

# Calculate the perimeter of the triangle
perimeter = side_a + side_b + side_c

# Display the result
print(f"The perimeter of the triangle is {perimeter}")

# Prompt user for the length and width of the rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Calculate the area and perimeter of the rectangle
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)

# Display the results
print(f"The area of the rectangle is {rectangle_area}")
print(f"The perimeter of the rectangle is {rectangle_perimeter}")

# Prompt user for the radius of the circle
radius = float(input("Enter radius: "))

# Calculate the area and circumference of the circle
pi = 3.14
circle_area = pi * radius * radius
circle_circumference = 2 * pi * radius

# Display the results
print(f"The area of the circle is {circle_area}")
print(f"The circumference of the circle is {circle_circumference}")

# Calculate the slope, x-intercept, and y-intercept of y = 2x - 2
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope

# Display the results
print(f"The slope is {slope}")
print(f"The x-intercept is {x_intercept}")
print(f"The y-intercept is {y_intercept}")

# Calculate the slope and Euclidean distance between points (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculate the slope
slope = (y2 - y1) / (x2 - x1)

# Calculate the Euclidean distance
euclidean_distance = ((x2 - x1)**2 + (y1 - y2)**2)**0.5

# Display the results
print(f"The slope between the points is {slope}")
print(f"The Euclidean distance between the points is {euclidean_distance}")

# Compare the slopes from tasks 8 and 9
slope_task_8 = 2  # Slope from y = 2x - 2
slope_task_9 = (y2 - y1) / (x2 - x1)  # Slope from points (2, 2) and (6, 10)

# Display the comparison
print(f"The slope from task 8 is {slope_task_8}")
print(f"The slope from task 9 is {slope_task_9}")
print(f"Are the slopes equal? {'Yes' if slope_task_8 == slope_task_9 else 'No'}")

# Calculate the value of y = x^2 + 6x + 9 for different x values
import math

def calculate_y(x):
    return x**2 + 6*x + 9

# Find the x value where y = 0
x_value = -3  # Solve x^2 + 6x + 9 = 0 (factorized as (x + 3)^2 = 0)
y_value = calculate_y(x_value)

# Display the results
print(f"For x = {x_value}, y = {y_value}")
print(f"The value of y is 0 when x = {x_value}")

# Find the length of 'python' and 'dragon'
python_length = len('python')
dragon_length = len('dragon')

# Make a falsy comparison statement
falsy_comparison = python_length != dragon_length

# Display the results
print(f"The length of 'python' is {python_length}")
print(f"The length of 'dragon' is {dragon_length}")
print(f"Is the length of 'python' not equal to 'dragon'? {falsy_comparison}")

# Correctly check if 'on' is in both 'python' and 'dragon'
contains_on = 'on' in 'python' and 'on' in 'dragon'

# Display the corrected result
print(f"Is 'on' found in both 'python' and 'dragon'? {contains_on}")

# Check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon."
contains_jargon = 'jargon' in sentence

# Display the result
print(f"Does the sentence contain the word 'jargon'? {contains_jargon}")

# Find the length of the text 'python'
python_length = len('python')

# Convert the length to float and then to string
python_length_float = float(python_length)
python_length_str = str(python_length_float)

# Display the results
print(f"The length of 'python' as a float is {python_length_float}")
print(f"The length of 'python' as a string is '{python_length_str}'")

# Check if a number is even
number = int(input("Enter a number: "))
is_even = number % 2 == 0

# Display the result
print(f"Is the number {number} even? {is_even}")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
floor_division_result = 7 // 3
int_converted_value = int(2.7)
comparison_result = floor_division_result == int_converted_value

# Display the result
print(f"Is the floor division of 7 by 3 equal to the int converted value of 2.7? {comparison_result}")

# Check if the type of '10' is equal to the type of 10
type_comparison = type('10') == type(10)

# Display the result
print(f"Is the type of '10' equal to the type of 10? {type_comparison}")

# Check if int('9.8') is equal to 10
try:
    result = int('9.8') == 10
except ValueError:
    result = False

# Display the result
print(f"Is int('9.8') equal to 10? {result}")

# Prompt user to enter hours and rate per hour
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))

# Calculate weekly pay
weekly_earning = hours * rate_per_hour

# Display the result
print(f"Your weekly earning is {weekly_earning}")

# Prompt user to enter the number of years they have lived
years_lived = int(input("Enter number of years you have lived: "))

# Calculate the number of seconds in the given years
seconds_lived = years_lived * 365 * 24 * 60 * 60

# Display the result
print(f"You have lived for {seconds_lived} seconds.")

# Display the table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")


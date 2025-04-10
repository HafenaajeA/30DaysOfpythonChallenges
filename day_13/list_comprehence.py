# Day 13 of 30 days of python challenges

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [i for i in numbers if i < 0]
print(negative_numbers)  

#==========

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [ number for row in list_of_lists for inner in row for number in inner]
print(flattened_list)

#===========

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

# 1. Create a list of tuples using list comprehension
number_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(number_tuples)

#=========

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
formatted_countries = [[country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries]
print(formatted_countries)

#=========================

# convert into dictionary
country_dicts = [{'country': country[0][0], 'code': country[0][0][:3].upper(), 'capital': country[0][1]} for country in countries]
print(country_dicts)

#=============

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{name[0][0]} {name[0][1]}" for name in names]
print(full_names)

#=====================

# Lambda function to calculate slope (m) given two points (x1,y1) and (x2,y2)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Lambda function to calculate y-intercept (b) using point-slope form
y_intercept = lambda x, y, m: y - (m * x)

# Example usage:
point1 = (2, 4)  # (x1, y1)
point2 = (6, 10) # (x2, y2)

m = slope(point1[0], point1[1], point2[0], point2[1])
b = y_intercept(point1[0], point1[1], m)

print(f"Slope (m): {m}")
print(f"Y-intercept (b): {b}")
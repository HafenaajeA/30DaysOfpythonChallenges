# Day 14 of 30 days of python challenge
# Higher Order Functions

# Higher order functions are functions that take other functions as arguments or return them as output.


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#exercises: Level 1

# 1. Explain the difference between map, filter, and reduce.
# map: applies a function to each item in an iterable and returns a new iterable with the results.
# filter: applies a function to each item in an iterable and returns a new iterable with only the items that return True.   

# reduce: applies a function to the items of an iterable cumulatively, reducing the iterable to a single value.

# 2. Explain the difference between higher order function, closure and decorator

# Higher order function: a function that takes other functions as arguments or returns them as output.

# Closure: a function that remembers the values of the variables in its lexical scope even when the function is executed outside that scope.

# Decorator: a function that takes another function and extends its behavior without explicitly modifying it.

# 3. Define a call function before map, filter or reduce, see examples

# The call function is used to call a function with a specified this value and arguments provided individually.

# It is not commonly used with map, filter, or reduce, but it can be used to call a function with a specific context.

# In the context of map, filter, or reduce, you can use call to invoke a function with a specific context if needed.
# However, in most cases, you would simply pass the function directly without using call.
# For example:

#def add(x, y):
#   return x + y 
# 
# 
# 
# 4. Use for loop to print each country in the countries list
# 
for country in countries:
    print(country)

# 5 Use for to print each name in the names list.

for name in names:
    print(name)

# 6 Use for to print each number in the numbers list.

for number in numbers:
    print(number)

# Exercises: Level 2

# 1. Use map to create a new list by applying a function to each item in the countries list.
def to_uppercase(country):
    return country.upper()

uppercase_countries = list(map(to_uppercase, countries))
print(uppercase_countries)

# Alternative using lambda function
# uppercase_countries = list(map(lambda x: x.upper(), countries))

# 

# Using map to square each number in the numbers list
def square(num):
    return num ** 2

squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Alternative using lambda function
# squared_numbers = list(map(lambda x: x ** 2, numbers))


# 

# Use map to change each name to uppercase in the names list
uppercase_names = list(map(lambda x: x.upper(), names))
print("Uppercase names:", uppercase_names)

# Use filter to filter out countries containing 'land'
countries_with_land = list(filter(lambda x: 'land' in x.lower(), countries))
print("Countries containing 'land':", countries_with_land)

# Use filter to filter out countries having exactly six characters
six_char_countries = list(filter(lambda x: len(x) == 6, countries))
print("Countries with 6 characters:", six_char_countries)

# Use filter to filter out countries containing six letters and more
long_countries = list(filter(lambda x: len(x) >= 6, countries))
print("Countries with 6 or more characters:", long_countries)

# Use filter to filter out countries starting with 'E'
e_countries = list(filter(lambda x: x.startswith('E'), countries))
print("Countries starting with E:", e_countries)

# Chain two or more list iterators
from functools import reduce
chain_result = list(
    map(lambda x: x.upper(),
        filter(lambda x: len(x) >= 6, countries))
)
print("Chained result:", chain_result)

# Function to get string lists
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

mixed_list = [1, 'Python', 2, 'JavaScript', 3, 'Java']
string_list = get_string_lists(mixed_list)
print("String items only:", string_list)

# Use reduce to sum all numbers
numbers_sum = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", numbers_sum)

# Use reduce to concatenate countries
def concat_countries(acc, curr):
    if acc == "":
        return curr
    if curr == countries[-1]:
        return f"{acc}, and {curr}"
    return f"{acc}, {curr}"

countries_sentence = reduce(concat_countries, countries, "") + " are north European countries"
print(countries_sentence)

# Function to categorize countries by pattern
def categorize_countries(countries_list, pattern):
    return list(filter(lambda x: pattern.lower() in x.lower(), countries_list))

# Function to count countries by first letter
def get_countries_dict(countries_list):
    return {
        letter: len([country for country in countries_list if country.startswith(letter)])
        for letter in set(country[0] for country in countries_list)
    }

# Assuming we have a larger countries list in countries.js
def get_first_ten_countries(countries_list):
    return countries_list[:10]

def get_last_ten_countries(countries_list):
    return countries_list[-10:]

# Example usage of the categorization functions
print("Countries with 'land':", categorize_countries(countries, 'land'))
print("Countries by first letter:", get_countries_dict(countries))

# Exercise 3 - Working with Countries Data
from countries_data import countries_data

def sort_countries_by_name(countries_list=countries_data):
    return sorted(countries_list, key=lambda x: x['name'])

def sort_countries_by_capital(countries_list=countries_data):
    return sorted(countries_list, key=lambda x: x.get('capital', ''))

def sort_countries_by_population(countries_list=countries_data):
    return sorted(countries_list, key=lambda x: x['population'], reverse=True)

def get_most_spoken_languages(countries_list=countries_data, top_n=10):
    # Create a dictionary to store language frequencies
    language_count = {}
    for country in countries_list:
        for language in country['languages']:
            language_count[language] = language_count.get(language, 0) + 1
    
    # Sort languages by frequency and get top N
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:top_n]

def get_most_populated_countries(countries_list=countries_data, top_n=10):
    sorted_countries = sorted(countries_list, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:top_n]

# Testing the functions
if __name__ == "__main__":
    print("\nCountries sorted by name (first 3):")
    for country in sort_countries_by_name()[:3]:
        print(f"{country['name']}")

    print("\nCountries sorted by capital (first 3):")
    for country in sort_countries_by_capital()[:3]:
        print(f"{country['name']}: {country.get('capital', 'No capital')}")

    print("\nTop 10 most populated countries:")
    for country in get_most_populated_countries():
        print(f"{country['name']}: {country['population']:,}")

    print("\nTop 10 most spoken languages:")
    for language, count in get_most_spoken_languages():
        print(f"{language}: {count} countries")

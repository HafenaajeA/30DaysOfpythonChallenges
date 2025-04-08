# Day 11 of 30 days of python  challenges

def add_two_numbers(num1, num2):
    sum =  num1  + num2
    return sum
print(add_two_numbers(2, 6))

#===========    

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area
print(area_of_circle(12))

#===========

def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            return f"Error: '{num}' is not a number"
    return total

# Test cases
print(add_all_nums(1, 2, 3))  # 6
print(add_all_nums(1, "2", 3))  # Error: '2' is not a number
print(add_all_nums(1, 2, 3, 4, 5, 6))  # 21
print(add_all_nums())  # 0

#===========


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(30))  # 86.0

#===========

def check_season(month):
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Fall'
    else:
        return "Invalid month"
print(check_season("March"))

#===========

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)"
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(1, 2, 3, 4))  # 1.0

#===========

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        return "No real roots"
print(solve_quadratic_eqn(1, -3, 2))  # (2.0, 1.0)

#===========

def print_list(lst):
    for item in lst:
        print(item)
print_list([1, 2, 3, 4, 5])  # Prints each number on a new line
#===========

def reverse_list(array):
    return array[::-1] 
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]

#===========

def capitalize_list_items(lst):
    return [item.capitalize() for item in lst] 
print(capitalize_list_items(['apple', 'banana', 'cherry']))  # ['Apple', 'Banana', 'Cherry']

#===========
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item([1, 2, 3], 4))  # [1, 2, 3, 4]

#===========
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
print(remove_item([1, 2, 3, 4], 3))  # [1, 2, 4]

#===========

def sum_of_numbers(lst):
    total = 0
    for num in lst:
        if isinstance(num, (int, float)):
            total += num
    return total

print(sum_of_numbers([1, 2, 3, 4, 5]))  # 15


#===========
    
def sum_of_odd_numbers(lst):
    total = 0
    for num in lst:
        if isinstance(num, (int, float)) and num % 2 != 0:
            total += num
    return total
print(sum_of_odd_numbers([1, 2, 3, 4, 5]))  # 9

#===========

def sum_of_even_numbers(lst):
    total = 0
    for num in lst:
        if isinstance(num, (int, float)) and num % 2 == 0:
            total += num
    return total
print(sum_of_even_numbers([1, 2, 3, 4, 5]))  # 6

#===========

# exercise level 2

def evens_and_odds(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"
print(evens_and_odds(100))  # 50 is even

#===========

def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
print(factorial(5))  # 120

#===========

def is_empty(lst):
    return len(lst) == 0
print(is_empty([]))  # True 

print(is_empty([1, 2, 3]))  # False

#===========

def calculate_mean(numbers):
    if not numbers:
        return "List is empty"
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    if not numbers:
        return "List is empty"
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid-1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def calculate_mode(numbers):
    if not numbers:
        return "List is empty"
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes[0] if len(modes) == 1 else modes

def calculate_range(numbers):
    if not numbers:
        return "List is empty"
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    if not numbers:
        return "List is empty"
    mean = calculate_mean(numbers)
    squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
    return squared_diff_sum / len(numbers)

def calculate_std(numbers):
    if not numbers:
        return "List is empty"
    return calculate_variance(numbers) ** 0.5

# Test cases
numbers = [1, 2, 3, 4, 5, 5, 6, 7]
print(f"Mean: {calculate_mean(numbers)}")  # 4.125
print(f"Median: {calculate_median(numbers)}")  # 4.5
print(f"Mode: {calculate_mode(numbers)}")  # 5
print(f"Range: {calculate_range(numbers)}")  # 6
print(f"Variance: {calculate_variance(numbers)}")  # ~3.859
print(f"Standard Deviation: {calculate_std(numbers)}")  # ~1.964

#===========

#Exercise : level 3

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(7))  # True      
print(is_prime(10))  # False

#===========

def is_unique(lst):
    return len(lst) == len(set(lst))
print(is_unique([1, 2, 3, 4]))  # True
print(is_unique([1, 2, 2, 4]))  # False

#===========

def same_data_type(lst):
    if not lst:
        return "List is empty"
    
    # Get the type of the first element
    first_type = type(lst[0])
    
    # Check if all elements are of the same type
    return all(isinstance(item, first_type) for item in lst)

# Test cases
print(same_data_type([1, 2, 3, 4]))  # True
print(same_data_type([1, "2", 3, 4]))  # False
print(same_data_type(["apple", "banana", "cherry"]))  # True
print(same_data_type([1.0, 2.0, 3.2]))  # True
print(same_data_type([]))  # "List is empty"

#===========

def is_valid_variable(name):
    """
    Check if a string is a valid Python variable name.
    Returns True if valid, False otherwise.
    """
    if not isinstance(name, str):
        return False
    
    # Check if string is empty
    if not name:
        return False
    
    # Check if first character is alphabetic or underscore
    if not (name[0].isalpha() or name[0] == '_'):
        return False
    
    # Check remaining characters are alphanumeric or underscore
    for char in name[1:]:
        if not (char.isalnum() or char == '_'):
            return False
    
    # Check if it's not a Python keyword
    import keyword
    if keyword.iskeyword(name):
        return False
    
    return True

# Test cases
print(is_valid_variable('firstname'))  # True
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('_name'))  # True
print(is_valid_variable('2name'))  # False
print(is_valid_variable('def'))  # False (keyword)
print(is_valid_variable(''))  # False
print(is_valid_variable('my-name'))  # False
print(is_valid_variable('my name'))  # False

#===========

from countries_data import countries_data

def most_spoken_languages(n=10):
    """
    Returns n most spoken languages in the world in descending order
    using data from countries-data.py
    """
    # Count language frequencies
    language_count = {}
    for country in countries_data:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    
    # Sort languages by frequency
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    
    # Return top n languages
    return [lang[0] for lang in sorted_languages[:n]]

# Test cases
print(most_spoken_languages())  # Default top 10
print(most_spoken_languages(20))  # Top 20

def most_populated_countries(n=10):
    """
    Returns n most populated countries in descending order
    Default returns top 10 countries if n is not specified
    """
    # Sort countries by population
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    
    # Return top n countries with name and population
    return [{'name': country['name'], 'population': country['population']} 
            for country in sorted_countries[:n]]

# Test cases
print(most_populated_countries())  # Default top 10
print(most_populated_countries(20))  # Top 20


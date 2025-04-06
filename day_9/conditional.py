# Exercise level 1

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more years to learn to drive")

my_age = 25
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {diff} years older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    if diff == 1:
        print("You are 1 year younger than me.")
    else:
        print(f"You are {diff} years younger than me.")
else:
    print("We are the same age.")


a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")



score = int(input("Enter your score: "))

if 80 <= score <= 100:
    print("Your grade is A")
elif 70 <= score <= 79:
    print("Your grade is B")
elif 60 <= score <= 69:
    print("Your grade is C")
elif 50 <= score <= 59:
    print("Your grade is D")
elif 0 <= score <= 49:
    print("Your grade is F")
else:
    print("Invalid score. Please enter a number between 0 and 100.")


month = input("Enter the month: ").strip().capitalize()

if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month. Please enter a valid month name.")

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ").strip().lower()

if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print("Fruit added! Modified list:", fruits)




person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if 'skills' key exists
if 'skills' in person:
    skills = person['skills']
    
    # Print middle skill
    mid_index = len(skills) // 2
    if len(skills) % 2 == 0:
        print("Middle skills:", skills[mid_index - 1], "and", skills[mid_index])
    else:
        print("Middle skill:", skills[mid_index])
    
    # Check if 'Python' is in skills
    has_python = 'Python' in skills
    print("Has Python skill:", has_python)

    # Determine developer title
    if skills == ['JavaScript', 'React']:
        print('He is a front end developer')
    elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']):
        print('He is a backend developer')
    elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
        print('He is a fullstack developer')
    else:
        print('Unknown title')

# Marital status and country
if person.get('is_marred') and person.get('country') == 'Finland':
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name} lives in Finland. He is married.")

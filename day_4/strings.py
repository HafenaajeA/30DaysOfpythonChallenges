# Day 4 of 30 Days of Python Programming
str1= [ 'Thirty', 'Days', 'Of', 'Python']
formated_str1 = ' '.join(str1)
#print(formated_str1)

str2 = [ 'Coding', 'For', 'All']
formated_str2 = ' '.join(str2)
#print(formated_str2)

company = 'Coding For All'
print(company)

print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[:6])
print(company.rfind('Coding'))
print(company.replace('Coding', 'Python'))
print(company.replace('All', 'Everyone'))
print(company.split(' '))

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
company_list = companies.split(', ')
print(company_list)

print(company[0])
print(company[-1])
print(company[10])

sentence= "Python For Everyone"
acronym = ''.join(word[0] for word in sentence.split()).upper()
print(acronym)

for_all = "Coding For All"
abbr= "".join(word[0] for word in for_all.split()).upper()
print(abbr)

print(company.index('C'))
print(company.find('F'))
print(company.rfind('l'))

word = "You cannot end a sentence with because because because is a conjunction"

print(word.index('because'))
print(word.rindex('because'))

phrase_to_remove = "because because because"
new_sentence = word.replace(phrase_to_remove, '').strip()
print(new_sentence)

print(word.index('because'))

word_to_remove = "because"
another_new_sentence = word.replace(word_to_remove, '').strip()
print(another_new_sentence)

print(company.startswith('Coding'))
print(company.endswith('Coding'))

remove_space = "  Coding For All      "
print(remove_space.strip())

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

python_libraries_with_harsh = ' #'.join(python_libraries)
print(python_libraries_with_harsh)

print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\tAge\tCountry\tCity\nAlmando\t250\tNamibia\tWindhoek\n')

radius = 10
area = 3.14 * radius ** 2
formated_string = f"The area of a circle with radius {radius} is {area:.2f}"
print(formated_string)
# The area of a circle with radius 10 is 314.00

a = 8
b = 6

print(f" {a} + {b} = {a + b}")
print(f" {a} - {b} = {a - b}") 
print(f" {a} * {b} = {a * b}")
print(f" {a} / {b} = {a / b:.2f}") 
print(f" {a} % {b} = {a % b}")
print(f" {a} // {b} = {a // b}")
print(f" {a} ** {b} = {a ** b}")
print(f" {a} == {b} = {a == b}")
print(f" {a} != {b} = {a != b}")
print(f" {a} > {b} = {a > b}")
print(f" {a} < {b} = {a < b}")
print(f" {a} >= {b} = {a >= b}")
print(f" {a} <= {b} = {a <= b}")



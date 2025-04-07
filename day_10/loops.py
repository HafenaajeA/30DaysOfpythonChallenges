# Day 10 of 30 python challenges


for i in range(0, 12):
     print(i)


count = 0
while count < 10:
    print(count)
    count = count + 1
print(count)


for i in range(10, -1, -1):
    print(i)


i = 10
while i >= 0:
    print(i)
    i -= 1


for i in range(1, 8):
    print('#' * i)


for i in range(8):
    print("# " * 8)


for i in range(11):
    print(f"{i} x {i} = {i * i}")


tech_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in tech_list:
    print(item)


for i in range(0, 101):
    if i % 2 == 0:
        print(i)


total = 0
for i in range(101):
    total += i
print("The sum of all numbers is", total)


even_sum = 0
odd_sum = 0

for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("The sum of all evens is", even_sum)
print("The sum of all odds is", odd_sum)


countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Estonia']


from countries import countries

for country in countries:
    if 'land' in country:
        print(country)


fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)
print(country)


countries_data = [
    {'name': 'CountryA', 'languages': ['English', 'French'], 'population': 500000},
    ...
]

from countries_data import countries_data

all_languages = set()

for country in countries_data:
    for language in country['languages']:
        all_languages.add(language)

print("Total number of unique languages:", len(all_languages))


from collections import Counter

language_counter = Counter()

for country in countries_data:
    for language in country['languages']:
        language_counter[language] += 1

most_spoken = language_counter.most_common(10)
print("Ten most spoken languages:")
for lang, count in most_spoken:
    print(f"{lang}: {count}")


sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)

print("Ten most populated countries:")
for country in sorted_countries[:10]:
    print(f"{country['name']}: {country['population']}")

# Day 5 of 30 days challenges

#Exercise: level 1

list = []
lst = ["Desk", "Chair", "Table", "Lamp", "sofa"]
total_items = len(lst)

first, middle, last = lst[0], lst[total_items // 2], lst[-1]
print(f"First item: {first}")
print(f"Middle item: {middle}")
print(f"Last item: {last}")

mixed_data_types = ["Almando", 34, 17.5, "single", "Tolla street"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
all_company = len(it_companies)

first, middle, last = it_companies[0], it_companies[all_company // 2], it_companies[-1]

print(f"First company: {first}" )
print(f"Middle company: {middle}" )
print(f"Last company: {last}" )

it_companies[1] = "DTS"

#print(it_companies)

it_companies.insert(4,"Adare technologies")

#print(it_companies)

it_companies[4] = it_companies[4].upper()
#print(it_companies)

new_it_companies = '#, '.join(it_companies)
#print(new_it_companies)

check = "ADARE TECHNOLOGIES"

if check in it_companies:
    print(f"{check} exist in the list")
else:
    print(f"{check} is not in the list!")

it_companies.sort()
#print(it_companies)

it_companies.sort(reverse=True)
#print(it_companies)

sliced_company = it_companies[3:]
#print(sliced_company)

sliced_company1 = it_companies[:-3]
#print(sliced_company1)

mid = len(it_companies) // 2

middle = it_companies[2] if len(it_companies) % 2 != 0 else it_companies[mid -1 : mid +1]

#print(middle)

print(it_companies)
it_companies.remove("Oracle")
print(it_companies)
it_companies.remove("ADARE TECHNOLOGIES")
print(it_companies)

it_companies.remove("Amazon")
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies
#print(it_companies)

#join the following list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
#print(joined_list)

full_stack[full_stack.index('Redux') + 1: full_stack.index('Redux') + 1] = ['Python', 'SQL']

print(full_stack)

# EXERCISE: lEVEL 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()

min_age = ages[0]
max_age = ages[-1]

ages.append(min_age)
ages.append(max_age)

ages.sort()

mid = len(ages) //2

if len(ages) % 2 != 0:
    median = ages[mid]
else:
    median = (ages[mid -1] + ages[mid]) /2

print(median)

average_age = sum(ages) / len(ages)
print(average_age)

age_range = max(ages) - min(ages)

# Print the result
print("Age range:", age_range)


# Compute absolute differences
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)

# Print results
print("Absolute difference (min - average):", min_diff)
print("Absolute difference (max - average):", max_diff)

#find the middle countries in the list below
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

countries.sort()
mid = len(countries) //2

if len(countries) % 2 != 0:
    middle_countries = [countries[mid]]
else:
    middle_countries = [countries[mid - 1], countries[mid]]
print("Middle country(ies):", middle_countries)


mid = (len(countries) + 1) // 2

first_half = countries[:mid]
second_half = countries[mid:]

print("First half:", first_half)
print()
print()
print()
print()
print("Second half:", second_half)


# unpack the list
euro_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, * scandic = euro_countries

print(f"first country: {first}")
print(f"second country: {second}")
print(f"third country: {third}")
print(f"scandic country: {scandic}")


# Yoo! This was a challenge. but any way congratulation to myself. i love how  i am progressing well.
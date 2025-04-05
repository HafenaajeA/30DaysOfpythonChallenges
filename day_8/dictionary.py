# Day 8 of 30 days of python challenges exercise

dict = {} #empty dictionary

dict_dog = {"name": "Anaconda", "color":"brown", "breed": "German sheperd", "legs": "four", "age": 15}

student_dict = {"first_name":"Almando", "last_name": "Hafenaaje","Gender":"Male","age":34, "marital_status":"Single", "Skill":["HTML", "CSS","JS","SASS","PYTHON", "BOOTSTRAP"],
"country":"Namibia", "city":"Windhoek", "address": {
    "street": "tolla street",
    "zipcode":"966601"
}}

print(len(student_dict))

skills = student_dict["Skill"]

# Print the skills
print("Skills:", skills)

# Check and print the data type
print("Type of 'Skill':", type(skills))

# Check if it's a list
print("Is 'Skill' a list?", isinstance(skills, list))

student_dict["Skill"].append("React")
student_dict["Skill"].append("TypeScript")
#print(student_dict)


#print(student_dict.keys())
#print(student_dict.values())

print(student_dict.items())

del student_dict["marital_status"]
print(student_dict)

del dict_dog
#print(dict_dog)


#Dictionary, are not so heavy though. thank you so much!
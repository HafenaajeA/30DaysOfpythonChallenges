# Day 6 of 30 days of python challenges

tlp = ()
sisters = ("Eveline",)
brother= ("Lineekela",)

siblings = sisters + brother
print(len(siblings))

family_members = list(siblings)
family_members.append("Mateus")
family_members.append("Ndamona")
print(family_members)

# Exercise: Level 2

first_sibling, second_sibling, father, mother = family_members
print(father)

fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("carrot", "onion", "potato", "cabbage")
animal_products = ("milk", "meat", "egg", "cheese")

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_it = list(food_stuff_tp)

#======================================

# Finding the middle index
length = len(food_stuff_tp)
middle_index = length // 2  # Integer division

# Slicing out the middle item(s)
if length % 2 == 1:  # Odd number of items
    middle_item_it = food_stuff_it[middle_index]
else:  # Even number of items
    middle_item_it = food_stuff_it[middle_index - 1 : middle_index + 1]
print("Middle item(s) in list:", middle_item_it)

#========================================

food_stuff_it[:3]
print(food_stuff_it[:3])
food_stuff_it[-3:]
print(food_stuff_it[-3:])

del food_stuff_tp
#print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Iceland" in nordic_countries)
print("Estonia" in nordic_countries)   


# This challenges was print awesome and I learnt a lot from it.
# I am looking forward to the next challenge. 

# Yours Almando Hafenaaje
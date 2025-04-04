# Day 7 of 30 days of Python challenge
# Sets

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercise: Level 1

print(len(it_companies))  # Convert list to set
it_companies.add('Twitter')
it_companies.update(['Instagram', 'Snapchat'])
it_companies.remove('Snapchat')

# The difference between remove and discard
# remove raises KeyError if the element is not found, while discard does not raise an error.

#Exercise: Level 2

A.union(B)  # Union of A and B
A.intersection(B)  # Intersection of A and B
A.issubset(B)  # A is subset of B
A.disjoint(B)  # A and B are disjoint sets
A.union(B)  # Union of A and B
B.union(A)  # Union of B and A
A.symmetric_difference(B)  # Symmetric difference of A and B

del A  # Delete set A

#Exercise: Level 3
age_set = set(age)  # Convert list to set 

print(f"length of the set: {len(age_set)}")
print(f"length of the list: {len(age)}")

#Explain the difference between the following data types:
# string, list, tuple, set
# string: A string is a sequence of characters enclosed in quotes. It is immutable.
# list: A list is a mutable sequence of elements enclosed in square brackets. It can contain duplicate elements.
# tuple: A tuple is an immutable sequence of elements enclosed in parentheses. It can contain duplicate elements.
# set: A set is an unordered collection of unique elements enclosed in curly braces. It does not allow duplicate elements.


sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()  # Split the sentence into words
unique_words = set(words)  # Convert the list of words to a set to get unique words

# Print results
print(f"Total words: {len(words)}")
print(f"Unique words: {len(unique_words)}")
print("The unique words are:", unique_words)


#Aweesome Python. Love what i'm seeing.
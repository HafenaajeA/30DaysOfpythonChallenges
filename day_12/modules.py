# Day 12 of 30 days python challenges

import random
import string

def random_user_id():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# Test the function
print(random_user_id())


#============



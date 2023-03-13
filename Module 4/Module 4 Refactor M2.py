import sys
import random
import string

#create function to generate random dictionary

def generate_random_dictionary():
    i = 0
    random_dictionary = {}
    while i < random.randint(2, 10):
        random_dictionary[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        i += 1
    return random_dictionary


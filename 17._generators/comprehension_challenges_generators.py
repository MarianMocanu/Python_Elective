import time
import os
import string

def clear(): return os.system("cls")

def timer(func):
    def wrapper(*args):
        start = time.time()
        val = func(*args)
        end = (time.time()) - start
        print(f'Time elapsed: {end}')
        return val
    return wrapper

# 1. Find all of the numbers from 1-1000 that are divisible by 7

@timer
def divisible_by_7(number):
    for i in range(1, number):
        if i % 7 == 0:
            yield i

@timer
def divisible_by_7_comp(number):
    return (i for i in range(1, number) if i % 7 == 0)

# 2. Find all of the numbers from 1-1000 that have a 3 in them

@timer
def has_3_in_loop():
    for i in range(1, 1000):
        if "3" in str(i):
            yield i

def has_3_in_comp():
    return (i for i in range(1, 1000) if "3" in str(i))

# 5. In a string made up of randomly generated words, 
# generate a list of all words that have less than 4 letters

def less_than_4(filename):
    return (word for word in open(filename).read().split() if len(word) < 4)

    for word in open(filename).read().split():
        if len(word) < 4:
            yield word

# 6. Use a dictionary comprehension to count the length of each word 
# in a sentence.

def word_length(filename):
    table = str.maketrans("", "", string.punctuation)
    dict = {key.lower(): len(key) for key in open(filename).read().translate(table).split()}
    return dict

# 7. Use a nested list comprehension to find all of the numbers from 1-1000 
# that are divisible by any single digit besides 1 (2-9)

def divisible_by_digit():
    for i in range(1, 1000):
        divisible = 1
        for j in range(1, 10):
            if(i % j != 0):
                divisible = 0
                j = 10
        if divisible == 1:
            yield i
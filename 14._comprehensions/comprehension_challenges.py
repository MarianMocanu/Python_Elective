from memory_profiler import profile
from time import time
import os
import string

def clear(): return os.system("cls")


def time_it(function):
    def wrapper(*args):
        start = time()
        function(*args)
        end = time()
        print(f'Execution of function took: {end - start} \n')

        return function(*args)

    return wrapper

# 1. Find all of the numbers from 1-1000 that are divisible by 7
@profile
@time_it
def divisible_by_7_loop():
    myList = []
    for i in range(1, 1000):
        if i % 7 == 0:
            myList.append(i)
    print(myList)


@profile
@time_it
def divisible_by_7_comp():
    print([i for i in range(1, 1000) if i % 7 == 0])


# 2. Find all of the numbers from 1-1000 that have a 3 in them
@profile
@time_it
def has_3_in_loop():
    myList = []
    for i in range(1, 1000):
        if "3" in str(i):
            myList.append(i)
    print(myList)

@profile
@time_it
def has_3_in_comp():
    print([i for i in range(1, 1000) if "3" in str(i)])

# 3. Count the number of spaces in a string
@profile
@time_it
def count_spaces_loop(filename):
    spaces = 0
    file = open(filename).read()
    for char in file:
        if char == " ":
            spaces = spaces + 1
    print(f'Number of spaces is {spaces} \n')
    


@profile
@time_it
def count_spaces_comp(filename):
    file = open(filename).read()
    print(f'Number of spaces is {sum(1 for char in file if char == " ")}')



# 4. Remove all of the vowels in a string
#slow
@profile
@time_it
def rm_vowels_loop1(filename):
    file = open(filename).read()
    vowels = ["a", "e", "i", "o", "u"]
    for char in file:
        if char in vowels:
            file = file.replace(char, "")

#medium
@profile
@time_it
def rm_vowels_loop2(filename):
    file = open(filename).read()
    vowels = ["a", "e", "i", "o", "u"]
    s = ""
    for char in file:
        if char not in vowels:
            s = s + "".join(char)

#fast
@profile
@time_it
def rm_vowels_comp(filename):
    file = open(filename).read()
    vowels = ["a", "e", "i", "o", "u"]
    string = ""
    string += ''.join([char for char in file if char not in vowels])


# 5. In a string made up of randomly generated words, 
# generate a list of all words that have less than 4 letters

@profile
@time_it
def less_than_4(filename):
    stringList = [word for word in open(filename).read().split() if len(word) < 4]
    return stringList


# 6. Use a dictionary comprehension to count the length of each word 
# in a sentence.

@profile
@time_it
def word_length(filename):
    table = str.maketrans("", "", string.punctuation)
    dict = {key.lower(): len(key) for key in open(filename).read().translate(table).split()}
    return dict

# 7. Use a nested list comprehension to find all of the numbers from 1-1000 
# that are divisible by any single digit besides 1 (2-9)

@profile
@time_it
def divisible_by_digit():
    myList = [i for i in range(1, 1000) for j in range (1, 10)]




# 8. For all the numbers 1-1000, use a nested list comprehension to find the highest single digit any of the numbers is divisible by

# 9. Multiples of 3 and 5: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.



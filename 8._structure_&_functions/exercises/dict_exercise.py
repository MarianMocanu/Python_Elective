
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Words exercise

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import time

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def word_count_dictionary(filename):
    import string
    table = str.maketrans('', '', string.punctuation)
    file = open(filename)
    wCount = dict()
    for line in file:
        words = line.lower().translate(table).split()
        for word in words:
            if not word in wCount.keys():
                wCount[word] = 1
            else:
                wCount[word] += 1
    return wCount


def print_words(filename):
    words = word_count_dictionary(filename)
    for key in words.keys():
        print(key, ':', words[key])


def get_count(myTuple): return myTuple[1]


def print_top(filename):
    wCount = word_count_dictionary(filename)
    words = sorted(wCount.items(), key=get_count, reverse=True)
    for word in words[:20]:
        print(word[0], ':', word[1])


def time_it(function):
    def wrapper(*args):
        start = time.time()
        function(*args)
        end = time.time()
        print(f'Execution of function took: {end - start}')

        # return function(*args)

    return wrapper


@time_it
def main():
    if len(sys.argv) != 3:
        print('usage: python words.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)





main()

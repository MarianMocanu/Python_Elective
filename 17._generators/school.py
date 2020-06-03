import random
import time
import os

def clear(): return os.system("cls")

def time_it(function):
    def wrapper(*args):
        start = time.time()
        function(*args)
        end = time.time()
        print(f'Execution of function took: {end - start}')

        return function(*args)

    return wrapper

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

@time_it
def students_list(num_students):
    students = []
    for i in range(num_students):
        students.append({"id": i, "name": random.choice(names), "major": random.choice(majors)})
    return students

@time_it
def students_generator(num_students):
    for i in range(num_students):
        yield {"id": i, "name": random.choice(names), "major": random.choice(majors)}
        
    # generator expression
    # ({"id": i, "name": random.choice(names), "major": random.choice(majors)} for i in range(num_students))

# people = students_list(1000000)
people = students_generator(1000000)

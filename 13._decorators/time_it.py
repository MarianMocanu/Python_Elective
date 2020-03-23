import time
import os
def clear(): return os.system("cls")

def time_it(function):
    def wrapper(*args):
        start = time.time()
        # time.sleep(1)
        function(*args)
        end = time.time()
        print(f'Execution of function took: {end - start}')

        return function(*args)

    return wrapper

@time_it
def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

add(1,2,3)
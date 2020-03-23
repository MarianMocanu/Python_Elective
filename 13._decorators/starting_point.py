import sys
from datetime import datetime


def log(function):
    def wrapper(*args):
        file = open("log.txt", "a+")
        file.write(f'{datetime.now()}, {args}, {function(*args)} \n')
        file.close()

        return function(*args)

    return wrapper


@log
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


@log
def printer(text):
    return text * 2

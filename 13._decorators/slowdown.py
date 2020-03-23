import time

def slowdown(function):
    def wrapper(arg):
        time.sleep(1)
        return function(arg)
    return wrapper

@slowdown
def countdown(n):
    if not n:
        print("Liftoff!")
    else:
        print(f'{n} secunde pana la final')
        return countdown(n - 1)
    

countdown(10)

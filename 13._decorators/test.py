import time

def countdown(n):
    time.sleep(1)
    if not n:
        return "Liftoff!"
    else:
        print(n, end=' ')
        return countdown(n - 1)
    
    
print(countdown(3))

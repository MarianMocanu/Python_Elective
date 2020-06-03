from time import sleep

def compute():
    val = []
    for i in range(10):
        sleep(.5)
        val.append(i)
    return val

class Compute:
    def __call__(self):
        val = []
        for i in range(10):
            sleep(.5)
            val.append(i)
        return val

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        returnValue = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return returnValue

class iterator:

    def __init__(self, *args):
        if len(args) == 1:
            self.max = args[0]
            self.min = 0
            self.step = 1

        elif len(args) == 2:
            self.min = args[0]
            self.max = args[1]
            self.step = 1

        elif len(args) == 3:
            self.min = args[0]
            self.max = args[1]
            self.step = args[2]

    def __iter__(self):
        self.index = self.min
        return self

    def __next__(self):
        result = self.index
        self.index += self.step
        if self.index > self.max:
            raise StopIteration()
        return result


import os
def clear(): return os.system("cls")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        if self.next is not None:
            return str(self.data) + ", " + str(self.next)
        else:
            return str(self.data)

    def __len__(self):
        if self.data is not None:
            if self.next is not None:
                return 1 + len(self.next)
            else:
                return 1
        else:
            return 0

    def __repr__(self):
        return f'{self.__dict__}'


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is not None:
            return "[" + str(self.head) + "]"
        else:
            return "[]"

    def __len__(self):
        if self.head is not None:
            return len(self.head)
        else:
            return 0

    def __repr__(self):
        return f'{self.__dict__}'

    def __getitem__(self, key):
        i = 0
        value = self.head

        if isinstance(key, int):
            # checking if the index is backwards
            if key < 0:
                key = len(self.head) + key
            # finding the right index and returning the data
            while value is not None:
                if i == key:
                    return value.data
                value = value.next
                i = i + 1
            raise IndexError(f'{type(self).__name__} index {key} out of range(0, {len(self)})')

        elif isinstance(key, slice):
            #creating a sequence with the all indeces
            rangeOfIndices = range(len(self))[key]

            #checking if all arguments are correctly received 
            isRangeIncreasing = rangeOfIndices.start <= rangeOfIndices.stop + 1 and rangeOfIndices.step > 0

            #creating an iterable object based upon the sequence with all indeces 
            rangeOfIndices = iter(rangeOfIndices) if isRangeIncreasing else reversed(rangeOfIndices)

            #creating a list in which we store the result to be returned
            result = []

            #creating a function which will append or insert into the list
            updateResultFunction = result.append if isRangeIncreasing else (lambda data: result.insert(0, data))

            try:
                searchingForKey = next(rangeOfIndices)
            except StopIteration:
                return result

            node = self.head
            for i, element in enumerate(self):
                if node is None:
                    break
                if i == searchingForKey:
                    updateResultFunction(node.data)

                    try:
                        searchingForKey = next(rangeOfIndices)
                    except StopIteration:
                        return result

                node = node.next

            return result

        raise ValueError(f'{type(self).__name__} can only be indexed with integers or slices (not {type(key)})')


lili = LinkedList()
lili.head = Node(1)
lili.head.next = Node("2nd")
lili.head.next.next = Node([3, 4, 5])
lili.head.next.next.next = Node(6)
lili.head.next.next.next.next = Node("7th")

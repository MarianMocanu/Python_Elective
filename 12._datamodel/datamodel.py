import os
clear = lambda: os.system("cls")

class myObject:
    def __init__(self):
        self.name = "Marian"

    def __repr__(self):
        return f'{self.__dict__}'
    
    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return self.name + other.name

class Deck:
    def __init__(self):
        self.cards = ["A", "K", 4, 7]

    def __getitem__(self, key):
        return self.cards[key]

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        return self.cards + other.cards

    def __repr__(self):
        return f"{self.__dict__}"
    
    def __str__(self):
        return self.cards

    def __setitem__(self, key, value):
        self.cards[key] = value
    
    def __delitem__(self, key):
        del self.cards[key]

class Animal:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printAnimal(self):
        print("{} is {} years old.".format(self.name, self.age))
        print("I am a {}.".format(Animal.species))

dog = Animal("Doggo", 5)
dog.printAnimal()
print(type(dog))
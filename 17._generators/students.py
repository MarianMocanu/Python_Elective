class Student:

    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.capitalize()

    def __add__(self, student):
        return Student('Anna the daugther', 1234)

    def __str__(self):
        return f'{self.name}, {self.cpr}'

    def __repr__(self):
            return f'{self.__dict__}'

class PythonStudents:

    def __init__(self):
        self.students = []

    def __add__(self, student):
        self.students.append(student)

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        index = self.last
        self.last += 1
        if self.last > len(self.students):
            raise StopIteration()
        return self.students[index]

gen = (print(i) for i in PythonStudents())
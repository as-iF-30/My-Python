C = 2020
class Person:
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born

    def getAge(self):
        return c - self.year_born

    def __str__(self):
        return '{} ({})'.format(self.name, self.getAge())

class Student(Person):
    def __init__(self, name, year_born):
        Person.__init__(self, name, year_born)
        self.knowledge = 0
    def study(self):
        self.knowledge += 1

a = Student('Asif', 1999)
a.study()
print(a.knowledge)

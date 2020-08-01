class Animal:
    def __init__(self, name):
        self.name = name
        print(name)
    def feed(self, food):
        print('animal',food)

class Dog(Animal):
    def __init__(self,name):
        self.name = name
    def feed(self,food):
        print('Dog', food)
        Animal.feed(self,food) #calling function of parent class
        Animal.__init__(self, 'hide') #calling parent init function
o = Dog('Bruno')
o.feed('biscuit')

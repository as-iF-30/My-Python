class Employee:
    def __init__(self, name, slary, id):
        self.name = name
        self._slary = slary
        self.__id = id
    def __str__(self):
        return '{}, {}, {}'.format(self.name, self._slary, self.__id)


o1 = Employee('Asif','8.5','4')
o1.name = 'Ajay'
o1._slary = '9.3' #to change protected instances
o1._Employee__id = 5 #to change private instances
print(o1)

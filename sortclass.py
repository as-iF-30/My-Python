class Fruit():
    def __init__ (self,name,price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

l = [Fruit('Apple',10), Fruit('Mango',5), Fruit('Blueberry',20)]
for i in sorted(l, key = Fruit.sort_priority):#or key = lambda x: x.sort_priority()
    print(i.name)

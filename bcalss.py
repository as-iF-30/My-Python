class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)
    def __add__(self, otherpoint):
        return Point(self.x + otherpoint.x, self.y + otherpoint.y)
    def __sub__(self, otherpoint):
        return Point(self.x - otherpoint.x, self.y + otherpoint.y)
    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx,my)

p1 = Point(5,10)
p2 = Point(15,20)
print(p1,p2)
print(p1+p2)
print(p1-p2)
print(p1.halfway(p2))

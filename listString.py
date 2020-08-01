a = 'abc'
b = '123'
l1 = list(a)
l2 = list(b)
print(l1,l2)
l3 = list(map(int,b))
print(l3)
l4 = ''.join(map(str,l3))
print(l4)

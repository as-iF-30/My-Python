a=['ram','shayam','luv','kush']
b=[1,8,7,3]
d='-'.join(a) # convert as a string
print(d)
a.reverse()
print(a)
c=sorted(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(a[1])
print(a[-1])
print(a[0:2])
print(len(a))
a.append('Bharat')
a.insert(1,'Bhavi')
a.insert(0,b)
a.remove('luv')
print(a)
c=a.pop()
print(c)
print(min(b))
print(max(b))
print(sum(b))
print(a.index('ram'))
print('ram' in a)
#for i in  a:
#for i in enumerate(a):
for i in enumerate(a,start=1):
    print(i)

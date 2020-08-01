from itertools import permutations
n1 = int(input())
n2 = int(input())
l = []
for i in range(n1,n2+1):
    f = 0
    if i>1:
        for j in range(2,(i//2)+1):
            if(i%j==0):
                f = 1;
                break
        if f == 0:
            l.append(i)
print(l)
c = []
for i in l:
    for j in l:
        if i!=j:
            m = str(i) + str(j)
            c.append(int(m))
l = []
for i in c:
    f = 0
    if i>1:
        for j in range(2,(i//2)+1):
            if(i%j==0):
                f = 1;
                break
        if f == 0:
            if i not in l:
                l.append(i)
x = min(l)
y = max(l)
t = len(l)
for i in range(t-2):
    z = x + y
    x,y = y,z
print(z)

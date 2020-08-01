n = int(input())
a = input()
b = a.split()
d = 0
c=list(map(int,b))
e = max(c)
print(e)
for i in range(0, n):
    if e == c[i]:
        d = d + 1
print(d)

l = []
for i in range(0,3):
    l.append(list(map(int, input().rstrip().split())))
s = 0
for i in range(0,3):
    s += sum(l[i])
print(abs(45-s))

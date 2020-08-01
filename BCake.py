# if your niece is turning 4 years old, and the cake will have  candles of height 4,1,1,3,
# she will be able to blow out 2 candles successfully, since the tallest candles are of height 4 and there are 2 such candles
n = int(input())
a = input()
b = a.split()
d = 0
c=list(map(int,b))
e = max(c)
for i in range(0, n):
    if e == c[i]:
        d = d + 1
print(d)

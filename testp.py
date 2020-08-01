n = int(input())
operation = int(input())
k = int(input())
l = list(map(int,input().split()))
while operation != 0:
    for i in range(len(l)-1):
        a = l[i]^l[i+1]
        l[i] = a
    operation -= 1
    l.pop()
print(l[k])

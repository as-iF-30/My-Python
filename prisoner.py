#hackerrank
def saveThePrisoner(n, m, s):
    s -=1
    if(n == 1):
        return 1
    if(m>n):
        m = m%n
    t = s + m
    if(t>n):
        t= t-n
        return t
    if(t==0):
        return n
    return t

t = int(input())
for t_itr in range(t):
    nms = input().split()
    n = int(nms[0])

    m = int(nms[1])

    s = int(nms[2])

    f = saveThePrisoner(n, m, s)
    print(f)

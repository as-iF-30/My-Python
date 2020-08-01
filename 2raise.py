def valueOf(a):
    if(a==1):
        return 1
    l = [3,7,15,31,63,127,255,511,1023,2047,4095,8191,16383,32767,65535,131071]
    for i in l:
        for j in range(1,20+1):
            m = i*j
            # print(i,j)
            if(a/m==1.0):
                return j
    for i in l:
        if(a%i==0):
            return int(a/i)




n = int(input())
f = []
for i in range(n):
    a = int(input())
    k = valueOf(a)
    f.append(k)
for i in f:
    print(i)

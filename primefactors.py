#smith number ..sum of digit and its primefactors
import math
def primeFactor(n):
    m = n
    l = []
    while(n%2==0):
        l.append(2)
        n = n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i==0):
            l.append(int(i))
            n = n/i
    if(n>2):
        l.append(int(n))
    s = 0
    for i in l:
        # print(s)
        if(len(str(i))>1):
            # print(i)
            s2 = sum(int(j) for j in str(i))
            s+=s2
        else:
            s+=i
    s1 = sum(int(i) for i in str(m))
    if(s==s1):
        return 1
    else:
        return 0

n = int(input())
print(primeFactor(n))

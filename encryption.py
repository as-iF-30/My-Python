#hackerrank
import math
def encryption(s):
    l = list(s)
    c = math.ceil(math.sqrt(len(l)))
    f = math.floor(math.sqrt(len(l)))
    for i in range(0,c):
        m = []
        for j in range(i,len(l)+1,c):
            try:
                m.append(l[j])
            except:
                continue
        n = ''.join(map(str,m))
        print(n,end=" ")


s = input()
encryption(s)

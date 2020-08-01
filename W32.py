import math
def primesquare(l=[]):
    for i in range(1,len(l)):
        a=l[i]
        c=0
        b=int(math.sqrt(a))
        for j in range(1,a+1):
            if a%j==0:
                c+=1
        if a==b*b:
            pass
        elif c==2:
            pass
        else:
            return False
    return True

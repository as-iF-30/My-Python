import math
def kaprekarNumbers(p, q):
    c = 0
    for i in range(p,q+1):
        # print("i",i)
        x = int(math.pow(i,2))
        z = str(x)
        j = int(len(z)/2)
        if(j<1):
            if(x==i):
                c+=1
                print(i,end=" ")
        else:
            a = int(z[:j]) + int(z[j:])
            if(a==i):
                c+=1
                print(i,end=" ")
    if(c==0):
        print("INVALID RANGE")

p = int(input())
q = int(input())
kaprekarNumbers(p,q)

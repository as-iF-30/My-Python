i1 = int(input())
j1 = int(input())
k1 = int(input())
n = int(input())
f = []
for i in range(0,i1+1):
    for j in range(0,j1+1):
        for k in range(0,k1+1):
            if((i+j+k)!=n):
                l = [i,j,k]
                f.append(l)
print(f)

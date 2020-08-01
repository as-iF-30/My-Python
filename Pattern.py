import sys
n=int(input())
m=n;
for i in range(0,n):
    for j in range(1,m):
        sys.stdout.write(" ")
    for k in range(i+1,0,-1):
        sys.stdout.write("#")
    m=m-1
    print()

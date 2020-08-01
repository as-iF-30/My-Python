# HackerRank
def catAndMouse(x, y, z):
    a = abs(x-z)
    b = abs(y-z)
    if(a>b):
        return 'Cat B'
    elif(a<b):
        return 'Cat A'
    elif(a==b):
        return 'Mouse C'

q = int(input())
for q_itr in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    result = catAndMouse(x, y, z)
    print(result)

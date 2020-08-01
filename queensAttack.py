#Hackerrank
def queensAttack(n, k, r_q, c_q, obstacles):
    print(r_q,c_q,obstacles)
    c = 0
    #North
    i = r_q
    j = c_q
    while(i!=1):
        i-=1
        l = []
        l.append(i)
        l.append(j)
        print(l)
        z = 0
        for x in obstacles:
            if(x==l):
                z +=1
                break
        if(z==1):
            break
        c+=1
    print('N:',c)
    #south
    i = r_q
    while(i!=n):
        i +=1
        l = []
        l.append(i)
        l.append(j)
        z = 0
        print(l)
        for x in obstacles:
            if(x==l):
                z +=1
                break
        if(z==1):
            break
        c+=1
    print('NS',c)
    #west
    i  = r_q
    while(j!=1):
        j-=1
        l = []
        l.append(i)
        l.append(j)
        print(l)
        z = 0
        for x in obstacles:
            if(x==l):
                z+=1
                break
        if(z==1):
            break
        c+=1
    print('NSW',c)
    #East
    j = c_q
    while(j!=n):
        j+=1
        l = []
        l.append(i)
        l.append(j)
        print(l)
        z = 0
        for x in obstacles:
            if(x==1):
                z+=1
                break
        if(z==1):
            break
        c+=1
    print('NSWE',c)
    #North-West
    j = c_q
    while(i!=1 and j!=1):
        i-=1
        j-=1
        l = []
        l.append(i)
        l.append(j)
        print(l)
        z = 0
        for x in obstacles:
            if(x==1):
                z+=1
                break
        if(z==1):
            break
        c+=1
    print('NSWE,NW',c)
    #South-East
    i = r_q
    j = c_q
    while(i!=n and j!=n):
        i+=1
        j+=1
        l = []
        l.append(i)
        l.append(j)
        print(l)
        z = 0
        for x in obstacles:
            if(x==1):
                z+=1
                break
        if(z==1):
            break
        c+=1
    print('NSWE,NW,SE',c)
    #South-West
    i = r_q
    j = c_q
    while(i!=n and j!=1):
        i+=1
        j-=1
        l = []
        l.append(i)
        l.append(j)
        print(l)
        z = 0
        for x in obstacles:
            if(x==1):
                z+=1
                break
        if(z==1):
            break
        c+=1
    print('NSWE,NW,SE,SW',c)
    #North East
    i = r_q
    j = c_q
    print(i,j)
    while(i!=1 and j!=n):
        i-=1
        j+=1
        l = []
        l.append(i)
        l.append(j)
        print(l)
        z = 0
        for x in obstacles:
            if(x==1):
                z+=1
                break
        if(z==1):
            break
        c+=1
    print('NSWE,NW,SE,SW,SE',c)
    return c



nk = input().split()
n = int(nk[0])
k = int(nk[1])
r_qC_q = input().split()
r_q = int(r_qC_q[0])
c_q = int(r_qC_q[1])
obstacles = []
for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))
result = queensAttack(n, k, r_q, c_q, obstacles)

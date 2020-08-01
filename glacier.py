import itertools

days = int(input())
cluster = int(input())

c = []
tw = 0
for i in range(cluster):
    l = list(input().split())
    c.append(l)
    tw += int(l[2])
galon = []
for j in c:
    j[1] = int(j[1])
    j[2] = int(j[2])
    galon.append([j[0], j [2]])

connection  = int(input())
con = []
for i in range(connection):
    l = list(input().split('_'))
    con.append(l)
def check(am):
    sum = 0
    for i,j  in itertools.zip_longest(c,galon):
        if(i[0] == am):
            sum += j[1]
            if(i[2]<= j[1]):
                sum += check(i[2])
            else:
                return sum
    return sum
for i in range(days):
    for j,k in itertools.zip_longest(c,galon):
        if(j[2]>=j[1]):
            j[2] -= j[1]
        else:
            # print(j[0])
            for f in con:
                if(f[1]==j[0]):
                    j[2] = 0
                    j[2] = k[1]
                    tw += k[1]
                    if(f[0] != 'F'):
                        ml = check(f[0])
                        tw += ml
                    else:
                        break
        # print(j,k)
print(tw)

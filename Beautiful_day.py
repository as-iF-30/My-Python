#hackerrank
def beautifulDays(i, j, k):
    count = 0
    for m in range(i,j+1):
        a = m
        l = list(map(int,str(m)))
        l.reverse()
        s = [str(n) for n in l]
        b = int("".join(s))
        if((a-b)%k==0):
            count +=1
    return count
ijk = input().split()

i = int(ijk[0])

j = int(ijk[1])

k = int(ijk[2])

result = beautifulDays(i, j, k)
print(result)

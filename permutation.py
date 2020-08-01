#hackerrank
def permutationEquation(p):
    l = []
    for i in range(1,len(p)+1):
        # print(i)
        m = p.index(i)
        m = p.index(m+1)
        l.append(m+1)
        # print(l)
    return l

print(permutationEquation([4,3,5,1,2]))

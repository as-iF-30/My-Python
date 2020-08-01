def findAnagram(s,p):
    s = list(s)
    p = list(p)
    q = p.copy()
    q.reverse()
    size = abs(len(s)-len(p))+1
    inc = len(p)
    l = []
    for i in range(0,size):
        if(s[i:i+inc] == p):
            l.append(i)
        elif(s[i:i+inc] == q):
            l.append(i)
    print(l)


print(findAnagram('abab','ab'))

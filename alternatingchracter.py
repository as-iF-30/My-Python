def alternatingCharacters(s):
    l = list(s)
    c = 0
    for i in range(len(l)):
        try:
            if(l[i]==l[i+1]):
                c+=1
        except:
            return c
    return c


n = int(input())
for i in range(n):
    a = input()
    print(alternatingCharacters(a))
# 5
# AAAA
# BBBBB
# ABABABAB
# BABABA
# AAABBB

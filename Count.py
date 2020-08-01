str_i = input()
l = []
c = []
c1 = []
s = []
for i in str_i:
    l.append(i)
str_m = ' '.join(map(str, l))
str_split = str_m.split()
str_set = set(str_split)
for i in str_set :
    c.append(i),c1.append(str_split.count(i))
n = max(c1)
for i in range(0,len(c1)):
    if(n==c1[i]):
        s.append(c[i])
if(len(s)>1):
    for i in range (0,len(l)):
        for j in range (0,len(s)):
            if(l[i]==s[j]):
                print(s[j])
        break;
else:
    print(' '.join(map(str,s)))

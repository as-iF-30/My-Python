s = input()
d = {}
result = ''
for i in s:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
# print(d)
s = sorted(d, key = lambda x: d[x], reverse = True)
for j in s:
    result += j * d[j]
# print(result)

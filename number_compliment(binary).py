a = 22
# d = int("{0:08b}".format(a))
d  = bin(a).replace("0b","")
l = []
for i in d:
    if(i=='0'):l.append('1')
    elif(i=='1'):l.append('0')
s = "".join(l)
print(int(s,2))

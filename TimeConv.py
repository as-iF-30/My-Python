#inpput format: 07:05:45PM
n=input()
b=int(n[:2])
if n[8:10]=='AM':
    if  b==12:
     print("00"+n[2:8])
    else:
        print(n[0:8])
elif n[8:10]=='PM':
    if b<12:
     print(str(int(n[:2]) + 12) + n[2:8])
    else:
        print(n[0:8])

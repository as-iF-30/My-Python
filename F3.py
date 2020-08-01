f = open("myfile.txt","r")
c=0
d=f.read()
for i in d:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        c=c+1
print("Vowels:",c)
l=[]
n=int(input("Enter Length "))
print("enter values:")
for j in range(n):
    l.append(int(input()))
print("in reverse order:")
for i in range(n-1,-1,-1):
    print(l[i])

import re
def gridSearch(G,P):
    x = c = 0
    for i in G:
        l = [m.start() for m in re.finditer(P[c],i)]
        print(l)
        if(len(l) != 0):
            if(c==0):
                c += 1
                x = l.copy()
            elif(set(l) & set(x) == set(l)):
                c+=1
                x = l.copy()
        else:
            c = 0
            l = [m.start() for m in re.finditer(P[c],i)]
            print(i,P[c])
            if(len(l) != 0):
                if(c==0):
                    c += 1
                    x = l.copy()
        if(c == len(P)):
            return 'YES'
    return 'NO'
# ------------------------------------------------------------------------------------
# def gridSearch(G, P):
#     # print(G,P)
#     x = c = 0
#     for i in G:
#         l  = i.find(P[c])
#         if(l!=-1 and c==0):
#             x = l
#             c+=1
#         elif(l!=-1 and x == l):
#             x = l
#             c+=1
#         else:
#             c = 0
#             l = i.find(P[c])
#             x = 0
#             if(l!=-1 and c==0):
#                 x = l
#                 c+=1
#         if(c==len(P)):
#             return 'Yes'
#         print(l,x,c)
#     return 'No'

e = int(input())
for i in range(e):
    n = list(map(int,input().split()))
    Gn = n[0]
    Gm = n[1]
    G = []
    P = []
    for i in range(Gn):
        a = input()
        G.append(a)
    n = list(map(int,input().split()))
    Pn = n[0]
    Pm = n[1]
    for i in range(Pn):
        a = input()
        P.append(a)
    print(gridSearch(G,P))

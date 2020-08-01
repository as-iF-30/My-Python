from math import *
# def squares(a,b):
#     c = 0
#     for i in range(a,b+1):
#         m = str(math.sqrt(i))
#         m = m[::-1].find('.')
#         if(m == 1):
#             c +=1
#     return c
# print(squares(3,9))
# def squares(a,b):
#     c = 0
#     for i in range(a,b+1):
#         m = int(math.sqrt(i))
#         n = pow(m,2)
#         if(n==i):
#             c+=1
#     return c
# q = int(input())
t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    a = ceil(sqrt(a))
    b = floor(sqrt(b))
    print(a,b)
    print(int(b-a) + 1)
# ceil -  Smallest integer not less than x
# floar - largest integer not greater than x

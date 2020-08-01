import math
def solve(n):
    a = 5*n*n + 4
    b = 5*n*n - 4
    s1 = int(math.sqrt(a))
    s2 = int(math.sqrt(b))
    if(s1*s1 == a or s2*s2 == b):
        return 'IsFibo'
    else:
        return 'IsNotFibo'
t = int(input())
for i in range(t):
    n = int(input())
    print(solve(n))

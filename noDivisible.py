#hackerrank
def nonDivisibleSubset(k,s):
    c = 0
    m = [0]*k
    for i in range(len(s)):
        n = s[i]%k
        m[n]+=1
    print(m)
    if(m[0]>0):
        c += 1
    for i in range(0,len(m)//2):
        if(i+1 != len(m)-i-1):
            n = max(m[i+1],m[len(m)-i-1])
            c  += n
        print(c)
    if(len(m)%2==0):
        if(m[len(m)//2]>0):
            c+=1
    return c

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
s = list(map(int, input().rstrip().split()))
print(nonDivisibleSubset(k, s))

#leetcode
def removekdigits(num,k):
    l = []
    c = k
    m  = 0
    for i in num:
        while c  and l  and l[-1] > i:
            m+=1
            l.pop()
            c-=1
        l.append(i)
    a = "".join(l[0:len(num)-k]).lstrip("0")
    if len(a):
        return a
    else:
        return "0"

num = input()
k = int(input())
print(removekdigits(num,k))

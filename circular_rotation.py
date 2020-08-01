#hackerank
def circularArrayRotation(a, k, queries):
    if(k>=len(a)):
        k = k % len(a)
    for i in range(k):
        l = []
        l.append(a[len(a)-1])
        l.extend(a[:len(a)-1])
        a = l.copy()
    for i in queries:
        print(a[i])


nkq = input().split()
n = int(nkq[0])
k = int(nkq[1])
q = int(nkq[2])
a = list(map(int, input().rstrip().split()))
queries = []
for _ in range(q):
    queries_item = int(input())
    queries.append(queries_item)
result = circularArrayRotation(a, k, queries)
# print(result)

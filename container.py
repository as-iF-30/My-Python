def organizingContainers(container):
    mr = []
    mc = []
    n = len(container)
    for i in range(0,n):
        mr.append(sum(container[i]))
        j = 0
        tot = 0
        for j in range(0,n):
            tot += container[j][i]
        mc.append(tot)
    mr.sort()
    mc.sort()
    if mr==mc:
        return "Possible"
    else:
        return "Impossible"

q = int(input())
for q_itr in range(q):
    n = int(input())

    container = []

    for _ in range(n):
        container.append(list(map(int, input().rstrip().split())))
    print(organizingContainers(container))

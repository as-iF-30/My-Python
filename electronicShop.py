# hackerRank
def getMoneySpent(keyboards, drives, b):
    [keyboards.remove(i) for i in keyboards if i>=b]
    [drives.remove(i) for i in drives if i>=b]
    r = []
    for i in keyboards:
        for j in drives:
            s = 0
            s = i + j
            if(s<=b):
                r.append(s)
    if not r:
        return -1
    else:
        return max(r)

bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
moneySpent = getMoneySpent(keyboards, drives, b)
print(moneySpent)

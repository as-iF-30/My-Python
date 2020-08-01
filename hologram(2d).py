def hourglassSum(arr):
    l = []
    for i in range(4):
        try:
            for j in range(i+4):
                s = 0
                try:
                    if(j+3<=6):
                        s += sum(arr[i][j:j+3])
                        s += arr[i+1][j+1]
                        b = arr[i+2][j:j+3]
                        s += sum(arr[i+2][j:j+3])
                        l.append(s)
                except:break
        except: break
    return max(l)
arr = []
for i in range(6):
    n = list(map(int,input().split()))
    arr.append(n)
print(hourglassSum(arr))

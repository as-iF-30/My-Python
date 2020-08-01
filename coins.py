Total = int(input())
for _ in range(Total):
    amount = int(input())
    i = [1]
    while(True):
        if sum(i)>=amount:
            print(len(i))
            break
        else:
            f = sum(i)
            i.append(f+1)

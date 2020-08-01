def countingValleys(n, s):
    level=valley=0
    for i in range(n):
        if(s[i]=='U'):
            level+=1
            if(level==0):
                valley+=1
        else:
            level-=1
        print(level,valley)

    return valley
n = int(input())

s = input()

result = countingValleys(n, s)
print(result)

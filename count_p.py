def primeCount(n):
    c = 0
    m = 1
    for num in range(1,n + 1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                # print(num)
                m *= num
                if(m>n):
                    return c
                c+=1
    return c

n = int(input())
print(primeCount(n))

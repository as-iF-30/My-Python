def getPermutation(n,k):
    fact = [1, 1]
    for i in range(2,10):
        fact.append(i*fact[-1])
    print(fact)

    def getP(n, k ):
        print('g')
        if n == 1:
            return "1"
        ans  = ""
        count = 0
        for i in range(1, n+1):
            count += fact[n-1]
            if count > k:
                ans += str(i)
                count -= fact[n-1]
                r = getP(n-1, k-count)
                print(r)
                for j in r:
                    if int(j)>=i:
                        ans += str(int(j)+1)
                    else:
                        ans += str(j)
                return ans
    return getP(n,k-1)
print(getPermutation(4,9))

def splitNum(s):
    splits = []
    i = 0
    while i < 2 ** (len(s)-1):
        b = str(bin(i))[2:]
        b = "0" * (len(s)-len(b)-1) + b + "0"
        p = 0
        r = ""
        while p < len(s):
            r += s[p]
            if b[p] == "1":
                r += ","
            p += 1

        nums = [int(x) for x in r.split(",")]
        splits.append(nums)
        i += 1

    return splits


def isPrime(n):
    if n < 2:
        return False

    for i in range(2,n):
        if (n % i == 0):
            return False

    return True


def areAllPrimes(s):
    for num in s:
        if not isPrime(num):
            return False

    return True


s = input()
for splits in splitNum(s):
    if areAllPrimes(splits):
        print(splits)

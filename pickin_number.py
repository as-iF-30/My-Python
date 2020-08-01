#hackerrank
def pickingNumbers(a):
    a.sort()
    freq = {}
    index = [0]
    previous_key = 0
    for items in a:
        freq[items] = a.count(items)
    for key in freq:
        i = abs(previous_key - key)
        if(previous_key != 0):
            if(i == 1):
                d = freq[previous_key] + freq[key]
                index.append(d)
        previous_key = key
    m = max(index)
    n = max(freq.keys(), key = (lambda k : freq[k]))
    n = freq[n]
    return max(n,m)
n = int(input())
a = list(map(int,input().rstrip().split()))
print(pickingNumbers(a))

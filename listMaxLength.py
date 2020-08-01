def findMaxLength(nums):
    d = {}
    s = 0
    c = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            c += 1
        else:
            c -= 1
        if c == 0:
            s = i + 1
        if c in d:
            s = max(s,i -d[c])
        else:
            d[c] = i
    # print(d)
    return s

print(findMaxLength([0,1,0]))

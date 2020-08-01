def progression(l=[]):
    if len(l) == 1 or len(l) == 2:
        return True
    a = l[2] - l[1]
    for i in range(3, len(l)):
        if l[i] - l[i - 1] == a:
            pass
        else:
            return False
    return True
print(progression([7,3,-1,-5]))
import copy
def matrixflip(myl, d):
    m=copy.deepcopy(myl)
    if d == 'h':
        p = m[0][0]
        m[0][0] = m[0][1]
        m[0][1] = p
        p = m[1][0]
        m[1][0] = m[1][1]
        m[1][1] = p
        return m
    elif d == 'v':
        p = m[0]
        m[0] = m[1]
        m[1] = p
        return m
    else:
        return m

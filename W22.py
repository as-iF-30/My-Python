def nestingdepth(s):
    c = 0
    b = 0
    for i in range(0, len(s)):
        if s[i] == '(':
            c += 1
            if c > b:
                b = c
        elif s[i] == ')':
            if c > 0:
                c -= 1
            else:
                return -1
    if c != 0:
        return -1

    return b


s = (input("Enter:"))
print(nestingdepth(s))

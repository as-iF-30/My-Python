# Function to check parentheses
def check(s):
    a = ["[","{","("]
    b = ["]","}",")"]
    l = []
    for i in s:
        if i in a:
            l.append(i)
        elif i in b:
            pos = b.index(i)
            if ((len(l) > 0) and
                (a[pos] == l[len(l)-1])):
                l.pop()
            else:
                return "No"
    if len(l) == 0:
        return "Yes"
    else:
        return "No"


s = '{[]{()}}'
print(check(s))

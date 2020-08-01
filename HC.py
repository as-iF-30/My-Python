def ok(x):
    l = []
    for i in range(1, x + 1):
        c = input()
        m = c.split(' ')
        l.append(list(m))
    no(l)


def no(y):
    for i in range(1, len(y)):
        for j in range(1, len(y)):
            if y[2][i] == y[2][j]:
                c = +1


a = int(input())
ok(a)

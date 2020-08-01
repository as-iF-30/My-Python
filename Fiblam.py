cube = lambda x: pow(x,3)

def fibonacci(n):
    l = []
    f = 0
    m = 1
    l.append(f)
    l.append(m)
    for i in range(0,n-2):
         p = f + m
         f = m
         m = p
         l.append(p)
    return l
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

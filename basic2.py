#max count element
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count))

def x( ):
	return 1, 2, 3, 4
a, b, c, d = x()
print(a, b, c, d)

class MyName:
	Skill, Santa, Upskill = range(3)
print(MyName.Skill)
print(MyName.Upskill)
print(MyName.Santa)

#store
n = 10
result = 1 < n < 20
print(result)
result = 1 > n <= 9
print(result)

#reverse
l = [1,2,3,4,5]
print(l[::-1])

#array rotation
g = []
g.extend(l[2:])
g.extend(l[:2])
print(g)


# counting 1 in bits in number
def countBits(num):
    r = [0]
    for i in range(1, num +1):
        r.append(r[i>>1] + int(i&1))
    return r

print(countBits(5))

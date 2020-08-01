import numpy
a = list(map(int,input().split()))
b = list(map(int,input().split()))
A = numpy.array(a)
B = numpy.array(b)
print(numpy.inner(A,B))
print(numpy.outer(A,B))

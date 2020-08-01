# import numpy
# def cutTheSticks(arr):
#     while(len(arr)!=0):
#         print(len(arr))
#         m = min(arr)
#         a = numpy.array(arr)
#         a = a - m
#         a = a[a!=0
#         arr = list(a)
# cutTheSticks([5,4,4,2,2,8])

# -----------------------------------------------------------------
# x = [1,2,3,2,2,0,2,3,4,0]
# a = list(filter((0).__ne__, x))
# print(a)
n=int(input())
a=list(map(int,input().split()))
while len(a)!=0:
    print(len(a))
    a=list(map(lambda x: x-min(a),a))
    a=list(filter(lambda x: x!=0,a))

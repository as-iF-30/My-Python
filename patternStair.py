n = int(input())
for i in range(1,n+1):
    s = n-i
    for k in range(s):
        print(' ',end='')
    for j in range(i):
        print('#',end='')
    print()
   #
  ##
 ###
####

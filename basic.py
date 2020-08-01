import math
i = 8
# power
j = i**2
j = math.pow(i,2)
# square root
j = math.sqrt(j)
# cuberoot
j = i**(1./3)
# ------
# d -integer f -float o 0ctal E exponetial
print("h%2d, hlo%5.2f" %(1,1111110.533))
# here in f 2 is width and 5 is starting
print("%7o"%(25))
print("%10.3E"%(356.08977))
h = 'hi'
print(h.center(12))
print(h.ljust(14))
print(h.rjust(12))
print('hi {0},hello{1},tkx {n},float {c:.2f}'.format('1',1,n =2,c =9.2324234))
# --------------------------------
s=str(input())
print(any(letter.isalnum() for letter in s))
print(any(letter.isalpha() for letter in s))
print(any(letter.isdigit() for letter in s))
print(any(letter.isupper() for letter in s))
print(any(letter.islower() for letter in s))

import re
str='Hello, Welcome to Chandigarh University, Block-14'
x=re.findall("[g-z0-9G-Z]",str)
print(x)
x=re.findall("[0-9]",str)
print(x)
x=re.findall("[^Helo]",str)
print(x)#print all things except h,l,e,o
x=re.findall("c.m",str)
print(x)
x=re.search('e',str)
print(x)
x=re.match('Hello',str)
print(x)
x=re.subn("Hello","HI",str)
print(x)
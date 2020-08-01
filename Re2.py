import re

str = 'Hello, Welcome to Chandigarh University, Block-14. Hello Student'
x = re.findall("Hello", str, re.I)
print("1)Findall:")
print(x)
print("2)Finditer:")
p = re.compile(r'Hello')
x = p.finditer(str)
for i in x:
    print(i)
print("3)Search:")
x = re.search('Welcome', str, re.I)
print(x)
print("4)Match:"),
x = re.match('Welcome', str)
print(x)
print("5)Subn:")
x = re.subn("Hello", "HI", str)
print(x)
print("1)Sub:")
x = re.sub("Hello", "Hi", str)
print(x)


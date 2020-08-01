import re
str="yogesh Kumar" \
    "Asif Ali"
p=re.compile(r'\b[a-z]\w*\s',re.I)
r=p.finditer(str)
for i in r:
    print(i)
# p=re.search(r'^a\w*',str,re.I)
# print(p)
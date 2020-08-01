Dict = {'name': 'Ram', 'age':25, 'courses':['Python','DBMS']}
print(Dict)
print(Dict['name'])
#print(Dict['phone'])#ERROR
print(Dict.get('phone'))
print(Dict.get('phone','nahi mila')) #default message or value
#Method 1
Dict['name']='Shyam'#update
Dict['Ph']=454545#insert
print(Dict)
#Method 2
Dict.update({'name':'Bharat','pr':'87575'})
print(Dict)
del Dict['pr']
print(Dict)
c=Dict.pop('Ph')
print(Dict,c)
print(len(Dict))
print(Dict.keys())
print(Dict.values())
print(Dict.items())
for key,value in Dict.items():
    print(key,value)
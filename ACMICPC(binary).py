import itertools
def acmTeam(topic,s):
    subject =  0
    ques = []
    t = list(itertools.combinations(topic,2))
    for i in t:
        c = i[0]|i[1]
        c = bin(c).replace("0b", "")
        ques.append(c)
        if(c.count('1')>subject):
            subject = c.count('1')
    print(subject)
    c = 0
    for i in ques:
        if(i.count('1')==subject):
            c+=1
    print(c)

n = list(map(int,input().split()))
topic = []
for i in range(n[0]):
    item = int(input(),2)
    topic.append(item)
acmTeam(topic,n[1])

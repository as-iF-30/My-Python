def minion_game(string):
    V = ['A', 'E', 'I', 'O', 'U']
    c = 0
    v = 0
    for i in range(len(string)):
        if(string[i] not in  V):
            c+=(len(string)-i)
        else:
            v+=(len(string)-i)

    if(c==v):
        print("Draw")
    elif(c>v):
        print("stuart",c)
    else:
        print("kevin",v)
if __name__ == '__main__':
    s = input()
    minion_game(s)

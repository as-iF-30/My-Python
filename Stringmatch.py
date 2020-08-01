def count_substring(string, sub_string):
    c = 0
    s = list(string)
    ss = list(sub_string)
    for i in range(0,len(s)):
        k=0
        if(s[i]==ss[0]):
            k+=1
            for j in range(1,len(ss)):
                if(i+j>=len(s)):
                    return c
                if(s[i+j]==ss[j]):
                    k+=1
            if(k==len(ss)):
                print(s[i])
                c+=1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

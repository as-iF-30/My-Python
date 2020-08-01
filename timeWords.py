#HackerRank

# import inflect
# def timeInWords(h,m):
#     p = inflect.engine()
#     if(m<=30):
#         hs = p.number_to_words(h)
#         ms = p.number_to_words(m)
#         if(m==0):
#             return hs+" o'clock"
#         elif(m==15):
#             return 'quater past ' + hs
#         elif(m==30):
#             return 'half past ' + hs
#         elif(m>0 and m<=20):
#             return ms+' minute past '+ hs
#         elif(m>20):
#             l = list(ms.split('-'))
#             ms = ' '.join(l)
#             return ms + ' minutes past ' + hs
#     elif(m>30):
#         h +=1
#         m = abs(60-m)
#         hs = p.number_to_words(h)
#         ms = p.number_to_words(m)
#         if(m==45):
#             return 'quater to ' + hs
#         elif(m>0 and m<=20):
#             return ms + ' to ' + hs
#         elif(m>20):
#             l = list(ms.split('-'))
#             ms = ' '.join(l)
#             return ms + ' to ' + hs
def timeInWords(h,m):
    dic = {1 : 'one', 2 : 'two',  3 :'three', 4:'four', 5:'five', 6: 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
           11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 16 : 'sixteen', 17 : 'sventeen', 18 : 'eighteen',
           19 : 'ninteen', 20 : 'twenty', 21 : 'twenty one', 22 : 'twenty two', 23 : 'twenty three', 24 : 'twenty four',
           25 : 'twenty five', 26:'twenty six', 27: 'twenty seven', 28:'twenty eight', 29:'twenty nine'}
    if(m==0):
        return dic[h] + " o' clock"
    elif(m==15):
        return 'quarter past ' + dic[h]
    elif(m==30):
        return 'half past ' + dic[h]
    elif(m==45):
        h +=1
        if(h==13):
            h = 1
        return 'quarter to '+ dic[h]
    elif(m==1):
        return dic[m] + ' minute past ' + dic[h]
    if(m>30):
        m = abs(60-m)
        h +=1
        if(h==13):
            h = 1
        if(m==1):
            return dic[m] + ' minute to ' + dic[h]
        return dic[m] + ' minutes to ' + dic[h]
    else:
        return dic[m] + ' minutes past ' + dic[h]

h = int(input())
m = int(input())
print(timeInWords(h,m))

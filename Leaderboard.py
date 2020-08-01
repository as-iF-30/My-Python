#Hacker rank question Climbing the Leaderboard (Medium)
import bisect
players = int(input())
players_score = list(map(int,input().rstrip().split()))
contestant = int(input())
contestant_score = list(map(int,input().rstrip().split()))
final_score = list(dict.fromkeys(players_score))
l = len(final_score)
final_score.sort()
cfinal_score = final_score.copy()
for i in contestant_score:
    if(i in final_score):
        print(abs(final_score.index(i)-l))
    else:
        bisect.insort(final_score,i)
        print(abs(l-final_score.index(i)+1))
    final_score = cfinal_score.copy()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# n = int(input())
# l = list(map(int,input().rstrip().split()))
# a = int(input())
# s = list(map(int,input().rstrip().split()))
# c = 1
# r =[1]
# for i in range(0,n-1):
#     if(l[i]==l[i+1]):
#         r.append(c)
#     else:
#         c+=1
#         (r.append(c))
# for i in range(0,a):
#     for j in range(0,n):
#         if(s[i]==l[j]):
#             print(r[j])
#             break;
#         elif(s[i]>l[j]):
#             print(r[j])
#             break;
#         elif(s[i]<l[-1]):
#             print(r[-1]+1)
#             break;

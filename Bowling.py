#!/bin/python3

import math
import os
import random
import re
import sys
l = list(input().rstrip().split())
score = strike_count = count = 0
print(l)
spare = ['1/','2/','3/','4/','5/','6/','7/','8/','9/']
for i in range(10):
    if(l[i]=='X'):
        score+=10
        if(count == 1 or count == 2):
            score += 10
        if(strike_count >= 2):
            score+=10
        count = 1
        strike_count+=1
    elif(l[i] in spare):
        score += 10
        if(count == 1):
            score += 10
        elif(count == 2):
            res = list(l[i])
            res = int(res[0])
            score += res
        if(strike_count >= 2):
            res = list(l[i])
            res = int(res[0])
            score+=res
        strike_count = 0
        count = 2
    else:
        num = l[i]
        res = list(map(int, str(num)))
        score += sum(res)
        if(count == 1):
            score+=sum(res)
            c = 0
        elif(count == 2):
            score += res[0]
            count = 0
        if(strike_count >= 2):
            score += res[0]
        strike_count = 0
        count = 0
print('Total Score:',score)
# X X 9/ 80 X X 90 8/ 7/ 44 -171
# X 7/ 72 9/ X X X 23 6/ 7/ - 165
# 8/ X 70 6/ 9/ X 8/ 2/ X 9/ - 165

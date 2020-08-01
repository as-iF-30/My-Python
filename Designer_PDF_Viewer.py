#hackerrank
import string
from collections import OrderedDict
def designerPdfViewer(h, word):
    dict = {}
    a=0
    l = []
    for i in string.ascii_lowercase:
        dict[i] = h[a]
        a+=1
    for i in word:
        l.append(dict[i])
    return max(l)*len(word)

h = list(map(int, input().rstrip().split()))
word = input()
print(designerPdfViewer(h,word))

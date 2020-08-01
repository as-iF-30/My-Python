from collections import Counter
def findAnagram(s1,s2):
    if len(s1)>len(s2):
        return False
    s1_counter = Counter(s1)
    w_c = Counter()
    for i,c in enumerate(s2):
        w_c[c] +=1
        if i>=len(s1):
            element_form_left = s2[i - len(s1)]
            if w_c[element_form_left] == 1:
                del w_c[element_form_left]
            else:
                w_c[element_form_left] -=1
        if w_c == s1_counter:
            return True
    return False
print(findAnagram('ab','eidbaooo'))

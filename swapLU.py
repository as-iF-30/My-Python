# def swap_case(s):
#     l = []
#     for i in s:
#         if(i.islower()):
#             i = i.upper()
#         elif(i.isupper()):
#             i = i.lower()
#         l.append(i)
#         s = ''.join(map(str,l))
#         # s = ''.join([str(i) for i in l])
#     print(s)
def change(x):
    if str.islower(x):
        return str.upper(x)
    else:
        return str.lower(x)
def swap_case(s):
    return ('').join(map(change,s))
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

import bisect
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)
bisect.insort(mylist,'d')
print(mylist)
print(list(set(mylist)))
# --------------------------------------------
l = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
m = {}
for i in l:
    m[i] = l.count(i)
print(max(m,key = m.get))
# lst = ['A', 'B', 'C']
# dict(map(reversed, enumerate(lst)))
# {'A': 0, 'C': 2, 'B': 1}

# >>> lst = ['A','B','C']
# >>> dict(zip(lst,range(len(lst))))
# test_list = ['Nikhil', 'Akshat', 'Akash', 'Manjeet']
#
# # printing original list
# print("The original list : " + str(test_list))
#
# # using Dictionary comprehension + enumerate()
# # Dictionary with index as value
# res = {val : idx + 1 for idx, val in enumerate(test_list)}
#
# # print result
# print("The Dictionary after index keys : " + str(res))
# res = dict(zip(test_list, range(1, len(test_list)+1)))

# print result
# print("The Dictionary after index keys : " + str(res))
# test_list.sort(key = lambda test_list: test_list[1])
# a = OrderedDict.fromkeys(string.ascii_lowercase,range(1,27))
# l = list(itertools.combinations(s,2)) to make sets
# -----------------------------------
# Find max count
 # res = max(set(nums), key = nums.count)

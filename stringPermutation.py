def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return 'no answer'

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    l = []
    [l.append(chr(i)) for i in arr]
    l = ''.join(l)
    return l
str = input()
l = list(str)
print(l)
arr = []
[arr.append(ord(i)) for i in l]
print(arr)
print(next_permutation(arr))

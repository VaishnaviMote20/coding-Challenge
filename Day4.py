import math
def merge(arr1, arr2):
    m, n = len(arr1), len(arr2)
    total_len = m + n
    gap = math.ceil(total_len / 2)

    while gap > 0:
        i, j = 0, gap
        while j < total_len:

            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]
            else:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

            i += 1
            j += 1
        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)

arr1, arr2 = [1, 3, 5], [2, 4, 6]
merge(arr1, arr2)
print(arr1, arr2)

arr1, arr2 = [10, 12, 14], [1, 3, 5]
merge(arr1, arr2)
print(arr1, arr2)

arr1, arr2 = [2, 3, 8], [4, 6, 10]
merge(arr1, arr2)
print(arr1, arr2)

arr1, arr2 = [1], [2]
merge(arr1, arr2)
print(arr1, arr2)  

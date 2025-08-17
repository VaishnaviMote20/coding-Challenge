def findDuplicate(arr):
    slow = arr[0]
    fast = arr[0]

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow

print(findDuplicate([1, 3, 4, 2, 2]))
print(findDuplicate([3, 1, 3, 4, 2]))
print(findDuplicate([1, 1]))
print(findDuplicate([1, 4, 4, 2, 3]))
print(findDuplicate(list(range(1, 100000)) + [50000]))

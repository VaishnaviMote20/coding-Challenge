def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = float('-inf')


    for i in range(n - 1, -1, -1):
        if arr[i] > max_from_right:  
            leaders.append(arr[i])
            max_from_right = arr[i]

    leaders.reverse()
    return leaders

print("Input: [1, 2, 3, 4, 0]")
print("Output:", find_leaders([1, 2, 3, 4, 0]))

print("Input: [7, 10, 4, 10, 6, 5, 2]")
print("Output:", find_leaders([7, 10, 4, 10, 6, 5, 2]))

print("Input: [5]")
print("Output:", find_leaders([5]))

print("Input: [100, 50, 20, 10]")
print("Output:", find_leaders([100, 50, 20, 10]))

print("Input: [1, 2, 3, ..., 1000000]")
print("Output:", find_leaders(list(range(1, 1000001))))

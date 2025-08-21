def trap(height):
    n = len(height)
    left, right = 0, n - 1
    leftMax, rightMax = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]
            right -= 1

    return water
if __name__ == "__main__":
    test_cases = [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),
        ([1,1,1], 0),
        ([5], 0),
        ([2,0,2], 2),]

    for height, expected in test_cases:
        result = trap(height)
        print(f"Input: {height}")
        print(f"Output: {result} (Expected: {expected})\n")

# Sqrt(x)
# Date: 2026-06-30

# Compute square root of x (integer part only).
# Example: 4 -> 2, 8 -> 2

###########################################
# Solution:
def my_sqrt(x):
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

###########################################
# Explanation:
# Binary search between 1 and x//2. Time: O(log x), Space: O(1).

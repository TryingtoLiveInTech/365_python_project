# Maximum Subarray
# Date: 2026-07-15

# Find the contiguous subarray with the largest sum.
# Example: [-2,1,-3,4,-1,2,1,-5,4] -> 6 (subarray [4,-1,2,1])

###########################################
# Solution:
def max_subarray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

###########################################
# Explanation:
# Kadane's algorithm: keep track of maximum sum ending at current position. Time: O(n), Space: O(1).

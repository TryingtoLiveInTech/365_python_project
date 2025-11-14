# Single Number
# Date: 2026-09-30

# Find the single number that appears once (others appear twice).
# Example: [2,2,1] -> 1

###########################################
# Solution:
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

###########################################
# Explanation:
# XOR all numbers. XOR of same numbers is 0, XOR with 0 is the number itself. Time: O(n), Space: O(1).

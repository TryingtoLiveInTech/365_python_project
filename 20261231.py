# Contains Duplicate
# Date: 2026-12-31

# Given an array of integers, return True if any value appears at least twice.
# Example: [1,2,3,1] -> True

###########################################
# Solution:
def contains_duplicate(nums):
    return len(nums) != len(set(nums))

###########################################
# Explanation:
# Convert to set and compare lengths. If lengths differ, there are duplicates. Time: O(n), Space: O(n).

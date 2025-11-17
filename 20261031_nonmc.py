# Remove Element
# Date: 2026-10-31

# Remove all instances of val in-place, return new length.
# Example: [3,2,2,3], val=3 -> length 2, array becomes [2,2,_,_]

###########################################
# Solution:
def remove_element(nums, val):
    write_index = 0
    for num in nums:
        if num != val:
            nums[write_index] = num
            write_index += 1
    return write_index

###########################################
# Explanation:
# Two-pointer: overwrite elements not equal to val. Time: O(n), Space: O(1).

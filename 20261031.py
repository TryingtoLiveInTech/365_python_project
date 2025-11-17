# Date: 2026-10-31
# Level: Medium

def remove_element(nums, val):
    write_index = 0
    for num in nums:
        if num != val:
            nums[write_index] = num
            write_index += 1
    return write_index

nums = [3, 2, 2, 3]
length = remove_element(nums, 3)
print(length, nums[:length])


# A. 2 [2, 2]
# B. 2 [3, 2]
# C. 4 [3, 2, 2, 3]
# D. 0 []

###########################################
# Answer: A
# Explanation: Two-pointer overwrites elements not equal to val. Elements [2,2] remain, length is 2. Array becomes [2,2,3,3] but only first 2 elements are valid.


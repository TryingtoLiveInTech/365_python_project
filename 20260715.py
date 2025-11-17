# Date: 2026-07-15
# Level: Medium

def max_subarray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([1]))
print(max_subarray([-1, -2, -3]))


# A. 6
#    1
#    -1
# B. 6
#    1
#    -3
# C. 4
#    1
#    -1
# D. 7
#    1
#    -1

###########################################
# Answer: A
# Explanation: Kadane's algorithm finds maximum sum of contiguous subarray. [-2,1,-3,4,-1,2,1,-5,4] has max sum 6 from [4,-1,2,1]. Single element returns itself. All negative returns least negative.


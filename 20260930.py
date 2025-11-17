# Date: 2026-09-30
# Level: Medium

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(single_number([1, 1, 2]))
print(single_number([4, 1, 2, 1, 2, 4, 3]))
print(single_number([5]))


# A. 2
#    3
#    5
# B. 0
#    0
#    5
# C. 1
#    3
#    5
# D. 2
#    1
#    5

###########################################
# Answer: A
# Explanation: XOR cancels pairs. [1,1,2]: 1^1^2 = 0^2 = 2. [4,1,2,1,2,4,3]: pairs cancel, leaves 3. Single element returns itself.


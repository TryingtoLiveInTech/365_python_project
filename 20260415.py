# Date: 2026-04-15
# Level: Medium

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(single_number([2, 2, 1]))
print(single_number([4, 1, 2, 1, 2]))
print(single_number([1]))


# A. 1
#    4
#    1
# B. 0
#    0
#    1
# C. 1
#    1
#    1
# D. 2
#    4
#    1

###########################################
# Answer: A
# Explanation: XOR operation: a^a=0, a^0=a. XORing all numbers cancels pairs, leaving the single number. [2,2,1] -> 2^2^1 = 0^1 = 1.


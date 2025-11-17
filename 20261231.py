# Date: 2026-12-31
# Level: Medium

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


# A. True
#    False
#    True
# B. True
#    True
#    True
# C. False
#    False
#    True
# D. True
#    False
#    False

###########################################
# Answer: A
# Explanation: Compare length of list vs set. If different, duplicates exist. [1,2,3,1] has duplicate (True). [1,2,3,4] no duplicates (False). [1,1,1,3,3,4,3,2,4,2] has duplicates (True).


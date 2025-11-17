# Date: 2026-11-30
# Level: Medium

def first_uniq_char(s):
    from collections import Counter
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

print(first_uniq_char('leetcode'))
print(first_uniq_char('aabb'))
print(first_uniq_char('abcabc'))


# A. 0
#    -1
#    -1
# B. 0
#    0
#    -1
# C. 1
#    -1
#    -1
# D. 0
#    -1
#    0

###########################################
# Answer: A
# Explanation: Returns index of first character with frequency 1. 'leetcode': 'l' at index 0. 'aabb' and 'abcabc' have no unique characters, return -1.


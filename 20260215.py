# Date: 2026-02-15
# Level: Medium

def first_uniq_char(s):
    from collections import Counter
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

print(first_uniq_char('leetcode'))
print(first_uniq_char('loveleetcode'))
print(first_uniq_char('aabb'))


# A. 0
#    2
#    -1
# B. 0
#    0
#    -1
# C. 1
#    2
#    -1
# D. 0
#    2
#    0

###########################################
# Answer: A
# Explanation: Counter counts frequencies. First unique character in 'leetcode' is 'l' at index 0, in 'loveleetcode' is 'v' at index 2, 'aabb' has no unique characters so returns -1.


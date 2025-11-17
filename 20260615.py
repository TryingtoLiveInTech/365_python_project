# Date: 2026-06-15
# Level: Medium

def first_uniq_char(s):
    from collections import Counter
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

print(first_uniq_char('aabbcc'))
print(first_uniq_char('abc'))
print(first_uniq_char(''))


# A. -1
#    0
#    -1
# B. 0
#    0
#    0
# C. -1
#    -1
#    -1
# D. 1
#    0
#    -1

###########################################
# Answer: A
# Explanation: Returns index of first character with frequency 1. 'aabbcc' has no unique chars (-1), 'abc' has 'a' at index 0, empty string returns -1.


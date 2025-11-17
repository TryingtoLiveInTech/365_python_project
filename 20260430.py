# Date: 2026-04-30
# Level: Medium

def str_str(haystack, needle):
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(str_str('mississippi', 'issip'))
print(str_str('abc', 'c'))
print(str_str('abc', 'd'))


# A. 4
#    2
#    -1
# B. 4
#    2
#    0
# C. 1
#    2
#    -1
# D. 4
#    3
#    -1

###########################################
# Answer: A
# Explanation: Sliding window finds first occurrence. 'issip' found at index 4 in 'mississippi'. 'c' at index 2 in 'abc'. 'd' not found returns -1.


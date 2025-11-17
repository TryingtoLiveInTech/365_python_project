# Date: 2026-10-15
# Level: Medium

def str_str(haystack, needle):
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(str_str('hello', 'll'))
print(str_str('aaaaa', 'bba'))
print(str_str('', ''))


# A. 2
#    -1
#    0
# B. 2
#    0
#    0
# C. 3
#    -1
#    0
# D. 2
#    -1
#    -1

###########################################
# Answer: A
# Explanation: Sliding window finds first occurrence. 'll' found at index 2 in 'hello'. 'bba' not in 'aaaaa' returns -1. Empty needle returns 0.


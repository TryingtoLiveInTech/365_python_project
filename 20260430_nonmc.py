# Implement strStr()
# Date: 2026-04-30

# Find first occurrence of needle in haystack.
# Example: haystack='hello', needle='ll' -> 2

###########################################
# Solution:
def str_str(haystack, needle):
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

###########################################
# Explanation:
# Sliding window: check each position if substring matches needle. Time: O(n*m), Space: O(1).

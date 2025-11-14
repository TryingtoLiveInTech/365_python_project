# Reverse String
# Date: 2026-03-15

# Write a function that reverses a string.
# Example: 'hello' -> 'olleh'

###########################################
# Solution:
def reverse_string(s):
    return s[::-1]

# Or using two pointers:
def reverse_string(s):
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

###########################################
# Explanation:
# Use slicing [::-1] for simplicity, or two-pointer technique. Time: O(n), Space: O(1) for two-pointer, O(n) for slicing.

# First Unique Character
# Date: 2026-06-15

# Find index of first non-repeating character.
# Example: 'leetcode' -> 0 (l is first unique)

###########################################
# Solution:
def first_uniq_char(s):
    from collections import Counter
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

###########################################
# Explanation:
# Count character frequencies, then find first character with count 1. Time: O(n), Space: O(n).

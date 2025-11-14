# Valid Parentheses
# Date: 2026-08-31

# Given a string containing just '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# Example: '()[]{}' -> True, '([)]' -> False

###########################################
# Solution:
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack

###########################################
# Explanation:
# Use a stack to track opening brackets. When encountering a closing bracket, check if it matches the most recent opening bracket. Time: O(n), Space: O(n).

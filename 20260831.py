# Date: 2026-08-31
# Level: Medium

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

print(is_valid('()[]{}'))
print(is_valid('([)]'))
print(is_valid('{[]}'))


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
# Explanation: Stack tracks opening brackets. '()[]{}' all match (True). '([)]' has mismatched order (False). '{[]}' properly nested (True).


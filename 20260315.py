# Date: 2026-03-15
# Level: Medium

def reverse_string(s):
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

print(reverse_string('hello'))
print(reverse_string('Python'))


# A. 'olleh'
#    'nohtyP'
# B. 'hello'
#    'Python'
# C. 'olleh'
#    'python'
# D. Error

###########################################
# Answer: A
# Explanation: Two-pointer technique swaps characters from both ends until pointers meet. 'hello' reversed is 'olleh', 'Python' reversed is 'nohtyP'.


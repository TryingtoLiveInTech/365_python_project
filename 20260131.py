# Date: 2026-01-31
# Level: Medium

def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x //= 10
    return x == reverted or x == reverted // 10

print(is_palindrome(1221))
print(is_palindrome(12321))
print(is_palindrome(10))


# A. True
#    True
#    False
# B. True
#    False
#    False
# C. False
#    True
#    False
# D. True
#    True
#    True

###########################################
# Answer: A
# Explanation: Reverse half the number. 1221: x=12, reverted=12 (True). 12321: x=12, reverted=123, x==reverted//10 (True). Numbers ending in 0 (except 0) return False.


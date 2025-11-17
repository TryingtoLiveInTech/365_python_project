# Date: 2026-11-15
# Level: Medium

def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x //= 10
    return x == reverted or x == reverted // 10

print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))


# A. True
#    False
#    False
# B. True
#    True
#    False
# C. False
#    False
#    False
# D. True
#    False
#    True

###########################################
# Answer: A
# Explanation: Reverse half the number mathematically. 121 reversed half is 1==1 (True). Negative numbers return False. Numbers ending in 0 (except 0) return False.


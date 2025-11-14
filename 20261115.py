# Palindrome Number
# Date: 2026-11-15

# Determine if an integer is a palindrome.
# Example: 121 -> True, -121 -> False

###########################################
# Solution:
def is_palindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

# Without converting to string:
def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x //= 10
    return x == reverted or x == reverted // 10

###########################################
# Explanation:
# Convert to string and reverse, or reverse half the number mathematically. Time: O(log n), Space: O(1) for math approach.

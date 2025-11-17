# Date: 2026-05-31
# Level: Medium

def is_palindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

print(is_palindrome(0))
print(is_palindrome(123))
print(is_palindrome(12321))


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
# Explanation: Convert to string and compare with reverse. 0 reversed is '0' (True). 123 reversed is '321' != '123' (False). 12321 reversed is '12321' (True).


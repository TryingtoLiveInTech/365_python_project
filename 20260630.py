# Date: 2026-06-30
# Level: Medium

def my_sqrt(x):
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

print(my_sqrt(9))
print(my_sqrt(15))
print(my_sqrt(0))


# A. 3
#    3
#    0
# B. 3
#    4
#    0
# C. 9
#    3
#    0
# D. 3
#    3
#    1

###########################################
# Answer: A
# Explanation: Binary search for integer square root. sqrt(9)=3, sqrt(15)=3 (largest integer with square <=15), sqrt(0)=0. Returns integer part only.


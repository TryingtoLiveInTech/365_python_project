# Date: 2026-09-19

count = 0

def increment():
    count += 1
    return count

print(increment())


# A. 1
# B. 0
# C. UnboundLocalError
# D. NameError

###########################################
# Answer: C
# Explanation: Need 'global count' to modify global variable.

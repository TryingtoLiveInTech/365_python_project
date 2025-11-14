# Date: 2026-09-11

x = 10

def func():
    print(x)
    x = 20

func()


# A. 10
# B. 20
# C. UnboundLocalError
# D. None

###########################################
# Answer: C
# Explanation: Local variable x is referenced before assignment.

# Date: 2026-06-28

class Test:
    x = 10
    
    def __init__(self):
        self.x = 20

t = Test()
print(t.x, Test.x)


# A. 10 10
# B. 20 20
# C. 20 10
# D. 10 20

###########################################
# Answer: C
# Explanation: Instance variable self.x shadows class variable Test.x. Instance gets 20, class still has 10.

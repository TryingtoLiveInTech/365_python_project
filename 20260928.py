# Date: 2026-09-28

class Callable:
    def __init__(self, value):
        self.value = value
    
    def __call__(self, x):
        return self.value + x

c = Callable(10)
print(c(5))


# A. 15
# B. 10
# C. 5
# D. TypeError

###########################################
# Answer: A
# Explanation: __call__ makes instances callable like functions. c(5) calls c.__call__(5).

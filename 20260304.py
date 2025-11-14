# Date: 2026-03-04

class Test:
    def method(self):
        return self

t = Test()
unbound = Test.method
bound = t.method
print(unbound is bound)


# A. True
# B. False
# C. Error
# D. None

###########################################
# Answer: B
# Explanation: Unbound method (class.method) and bound method (instance.method) are different objects.

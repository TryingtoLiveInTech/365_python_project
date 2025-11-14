# Date: 2026-03-28

class Test:
    def method(self):
        return 'called'

t = Test()
print(Test.method(t))


# A. called
# B. Error
# C. None
# D. <bound method>

###########################################
# Answer: A
# Explanation: You can call instance methods by passing the instance as the first argument to the class method.

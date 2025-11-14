# Date: 2026-09-08

class Test:
    @classmethod
    def method(cls):
        return cls.x
    
    x = 10

t = Test()
print(t.method())


# A. 10
# B. AttributeError
# C. None
# D. Error

###########################################
# Answer: A
# Explanation: Class methods can access class variables via cls parameter. cls.x refers to Test.x.

# Date: 2026-04-08

def add_method(cls):
    cls.new_method = lambda self: 'added'
    return cls

@add_method
class Test:
    pass

t = Test()
print(t.new_method())


# A. added
# B. Error
# C. None
# D. <lambda>

###########################################
# Answer: A
# Explanation: Class decorators can modify or add attributes to a class before it's used.

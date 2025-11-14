# Date: 2026-09-04

class Descriptor:
    def __get__(self, obj, objtype=None):
        return 'get'
    
    def __set__(self, obj, value):
        print(f'set: {value}')

class Test:
    attr = Descriptor()

t = Test()
print(t.attr)
t.attr = 10


# A. get
#    set: 10
# B. get
#    10
# C. Error
# D. None
#    set: 10

###########################################
# Answer: A
# Explanation: Descriptors control attribute access. __get__ is called on access, __set__ on assignment.

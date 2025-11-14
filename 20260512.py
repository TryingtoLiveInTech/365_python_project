# Date: 2026-05-12

class MyClass:
    x = 10
    
    @classmethod
    def class_method(cls):
        return cls.x
    
    @staticmethod
    def static_method():
        return MyClass.x

print(MyClass.class_method(), MyClass.static_method())


# A. 10 10
# B. Error
# C. None None
# D. <bound method> <function>

###########################################
# Answer: A
# Explanation: Both can access class variables. classmethod receives cls, staticmethod doesn't receive self or cls.

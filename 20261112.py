# Date: 2026-11-12

class MyClass:
    class_var = 0
    
    def __init__(self):
        self.instance_var = 0

obj1 = MyClass()
obj2 = MyClass()
obj1.class_var = 1
obj1.instance_var = 1
print(obj2.class_var, obj2.instance_var)


# A. 0 0
# B. 1 0
# C. 1 1
# D. 0 1

###########################################
# Answer: A
# Explanation: obj1.class_var = 1 creates an instance variable, not modifying the class variable. obj2.class_var still refers to the original class variable.

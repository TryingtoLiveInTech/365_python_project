# Date: 2026-10-12

class A:
    def method(self):
        return 'A'

class B(A):
    def method(self):
        return super().method() + 'B'

b = B()
print(b.method())


# A. A
# B. AB
# C. B
# D. Error

###########################################
# Answer: B
# Explanation: super() calls the parent class method, so it returns 'A' + 'B' = 'AB'.

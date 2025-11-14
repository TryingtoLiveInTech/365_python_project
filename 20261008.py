# Date: 2026-10-08

class A:
    def method(self):
        return 'A'

class B(A):
    def method(self):
        return 'B'

class C(A):
    def method(self):
        return 'C'

class D(B, C):
    pass

d = D()
print(d.method())


# A. A
# B. B
# C. C
# D. Error

###########################################
# Answer: B
# Explanation: Method Resolution Order (MRO) follows D -> B -> C -> A. B's method is found first.

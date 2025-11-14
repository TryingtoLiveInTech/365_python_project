# Date: 2026-10-28

class A:
    def method(self):
        return 'A'

class B(A):
    def method(self):
        return 'B'

class C(A):
    pass

b = B()
c = C()
print(b.method(), c.method())


# A. B A
# B. A B
# C. B B
# D. Error

###########################################
# Answer: A
# Explanation: B overrides method() from A, so b.method() returns 'B'. C doesn't override, so c.method() returns 'A'.

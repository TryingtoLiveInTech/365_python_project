# Date: 2026-12-28

class Test:
    def __init__(self):
        self.__private = 10
        self.public = 20

t = Test()
print(t.__private)


# A. 10
# B. 20
# C. AttributeError
# D. None

###########################################
# Answer: C
# Explanation: Names starting with __ are name-mangled. Access via t._Test__private, not t.__private.

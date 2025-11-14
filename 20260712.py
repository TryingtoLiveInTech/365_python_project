# Date: 2026-07-12

class Test:
    def __init__(self):
        return 'hello'

t = Test()
print(t)


# A. hello
# B. <__main__.Test object>
# C. TypeError
# D. None

###########################################
# Answer: C
# Explanation: __init__ cannot return a value (except None). Returning anything else raises TypeError.

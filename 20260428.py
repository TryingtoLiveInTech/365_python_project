# Date: 2026-04-28

class Test:
    def __getattr__(self, name):
        return f'Missing: {name}'

t = Test()
print(t.x, t.y)


# A. Missing: x Missing: y
# B. AttributeError
# C. None None
# D. Error

###########################################
# Answer: A
# Explanation: __getattr__ is called only when attribute is not found through normal lookup.

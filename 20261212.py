# Date: 2026-12-12

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'

p = Point(1, 2)
print(str(p), repr(p))


# A. (1, 2) (1, 2)
# B. (1, 2) Point(1, 2)
# C. Point(1, 2) (1, 2)
# D. Error

###########################################
# Answer: B
# Explanation: __str__ is for user-friendly output, __repr__ is for developer representation (ideally can recreate object).

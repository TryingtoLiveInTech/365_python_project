# Date: 2026-08-28

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError
        self._radius = value

c = Circle(5)
c.radius = -1
print(c.radius)


# A. -1
# B. 5
# C. ValueError
# D. AttributeError

###########################################
# Answer: C
# Explanation: The setter validates input and raises ValueError for negative values.

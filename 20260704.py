# Date: 2026-07-04

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

c = Circle(5)
print(c.area())


# A. 0
# B. TypeError
# C. None
# D. 25

###########################################
# Answer: B
# Explanation: Circle doesn't implement abstract method area(), so instantiating Circle raises TypeError.

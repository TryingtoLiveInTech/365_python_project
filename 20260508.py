# Date: 2026-05-08

class Counter:
    count = []
    
    def add(self, item):
        self.count.append(item)

c1 = Counter()
c2 = Counter()
c1.add(1)
print(c2.count)


# A. []
# B. [1]
# C. Error
# D. None

###########################################
# Answer: B
# Explanation: Mutable class variables are shared across all instances. Modifying through one instance affects all.

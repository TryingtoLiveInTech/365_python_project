# Date: 2026-11-05

gen = (i for i in range(3))
print(list(gen))
print(list(gen))


# A. [0,1,2]
#    [0,1,2]
# B. [0,1,2]
#    []
# C. Error
# D. [0,1,2]
#    None

###########################################
# Answer: B
# Explanation: Generators are exhausted after first iteration.

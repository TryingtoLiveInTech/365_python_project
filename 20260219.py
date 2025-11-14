# Date: 2026-02-19

lst = [1, 2, 3, 4]
for i in lst:
    if i % 2 == 0:
        lst.remove(i)
print(lst)


# A. [1, 3]
# B. [1, 2, 3, 4]
# C. [2, 4]
# D. Error

###########################################
# Answer: B
# Explanation: Modifying list while iterating can skip elements.

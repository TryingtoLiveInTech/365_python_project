# Date: 2026-06-10

a = [[1, 2], [3, 4]]
b = a.copy()
b[0][0] = 99
print(a)


# A. [[1, 2], [3, 4]]
# B. [[99, 2], [3, 4]]
# C. Error
# D. [[99, 2]]

###########################################
# Answer: B
# Explanation: copy() is shallow, nested lists are shared.

# Date: 2026-05-06

for i, val in enumerate(['a', 'b'], 1):
    print(i, val)


# A. 0 a
#    1 b
# B. 1 a
#    2 b
# C. (0, 'a')
#    (1, 'b')
# D. Error

###########################################
# Answer: B
# Explanation: enumerate(iterable, start) starts counting from start.

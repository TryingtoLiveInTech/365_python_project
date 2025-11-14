# Date: 2026-09-22

d = {1: 'a'}
print(d.get(2, 'default'), d[2])


# A. default default
# B. default KeyError
# C. None default
# D. Error

###########################################
# Answer: B
# Explanation: get() returns default, [] raises KeyError.

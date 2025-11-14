# Date: 2026-10-22

def append_item(item, lst=[]):
    lst.append(item)
    return lst

print(append_item(1))
print(append_item(2))


# A. [1]
#    [2]
# B. [1]
#    [1, 2]
# C. [1, 2]
#    [1, 2]
# D. Error

###########################################
# Answer: B
# Explanation: Mutable default arguments are shared across function calls.

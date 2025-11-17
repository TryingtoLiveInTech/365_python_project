# Date: 2026-09-15
# Level: Medium

def count_and_say(n):
    if n == 1:
        return '1'
    prev = count_and_say(n - 1)
    result = []
    count = 1
    for i in range(1, len(prev)):
        if prev[i] == prev[i-1]:
            count += 1
        else:
            result.append(str(count) + prev[i-1])
            count = 1
    result.append(str(count) + prev[-1])
    return ''.join(result)

print(count_and_say(1))
print(count_and_say(2))
print(count_and_say(3))


# A. '1'
#    '11'
#    '21'
# B. '1'
#    '1'
#    '1'
# C. '1'
#    '11'
#    '12'
# D. '1'
#    '2'
#    '3'

###########################################
# Answer: A
# Explanation: n=1: '1'. n=2: count '1' -> '11'. n=3: count '11' -> two 1s -> '21'. Each term describes previous term.


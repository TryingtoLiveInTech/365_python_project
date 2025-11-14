# Count and Say
# Date: 2026-09-15

# Generate nth term of count-and-say sequence.
# Example: n=4 -> '1211' (one 1, one 2, two 1s)

###########################################
# Solution:
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

###########################################
# Explanation:
# Recursively generate previous term, then count consecutive digits. Time: O(2^n), Space: O(2^n).

# Roman to Integer
# Date: 2026-07-31

# Convert Roman numeral to integer.
# Example: 'IV' -> 4, 'LVIII' -> 58

###########################################
# Solution:
def roman_to_int(s):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for char in reversed(s):
        value = values[char]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total

###########################################
# Explanation:
# Process from right to left. If current value < previous, subtract; otherwise add. Time: O(n), Space: O(1).

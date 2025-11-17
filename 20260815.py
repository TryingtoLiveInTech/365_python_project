# Date: 2026-08-15
# Level: Medium

def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

nums1 = [1, 2, 3, 0, 0, 0]
merge(nums1, 3, [2, 5, 6], 3)
print(nums1)


# A. [1, 2, 2, 3, 5, 6]
# B. [1, 2, 3, 2, 5, 6]
# C. [2, 5, 6, 1, 2, 3]
# D. [1, 2, 3, 0, 0, 0]

###########################################
# Answer: A
# Explanation: Merge backwards from end of arrays. Compare elements and place larger at end, working backwards. Result: [1, 2, 2, 3, 5, 6].


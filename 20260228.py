# Date: 2026-02-28
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

nums1 = [4, 5, 6, 0, 0, 0]
merge(nums1, 3, [1, 2, 3], 3)
print(nums1)


# A. [1, 2, 3, 4, 5, 6]
# B. [4, 5, 6, 1, 2, 3]
# C. [1, 2, 3, 0, 0, 0]
# D. [4, 5, 6, 0, 0, 0]

###########################################
# Answer: A
# Explanation: Merge backwards from end. Compare [4,5,6] and [1,2,3] from right, place larger elements at end. Result: [1, 2, 3, 4, 5, 6].


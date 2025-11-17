# Merge Sorted Arrays
# Date: 2026-08-15

# Merge two sorted arrays in-place.
# nums1 has enough space at the end for nums2.
# Example: nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3
# Result: [1,2,2,3,5,6]

###########################################
# Solution:
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

###########################################
# Explanation:
# Start from the end of both arrays and merge backwards. Time: O(m+n), Space: O(1).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a1, a2 = nums1, nums2
        if len(a1) > len(a2):
            a1, a2 = a2, a1
        l1, l2 = len(a1), len(a2)
        half = (l1 + l2 + 1) // 2
        l, r = 0, l1

        while l < r:
            i = l + (r - l) // 2
            j = half - i
            a1_right = a1[i] if i < l1 else float('inf')
            a2_left  = a2[j-1] if j > 0 else float('-inf')

            if a1_right >= a2_left:
                r = i
            else:
                l = i + 1
        
        i = l
        j = half - i

        left = max(
            a1[i - 1] if i > 0 else float('-inf'),
            a2[j - 1] if j > 0 else float('-inf'),
        )
        if (l1 + l2) % 2 == 1:
            return float(left)

        right = min(
            a1[i] if i < l1 else float('inf'),
            a2[j] if j < l2 else float('inf'),
        )
        return (left + right) / 2

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Only swap if needed — ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)  # m = smaller, n = larger
        total_left = (m + n) // 2

        lo, hi = 0, m                  # binary search on smaller array

        while lo <= hi:
            cut1 = (lo + hi) // 2
            cut2 = total_left - cut1

            l1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            r1 = nums1[cut1]     if cut1 < m else float('inf')
            l2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            r2 = nums2[cut2]     if cut2 < n else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 1:
                    return float(min(r1, r2))
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                hi = cut1 - 1
            else:
                lo = cut1 + 1
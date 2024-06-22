class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        # This solution is O(n) time rather than O(log(n)). Will update in future

        # Merge lists
        p1, p2 = 0, 0
        merged = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                merged.append(nums1[p1])
                p1 += 1
            
            else:
                merged.append(nums2[p2])
                p2 += 1

        if p1 < len(nums1): merged += nums1[p1:]
        elif p2 < len(nums2): merged += nums2[p2:]
        print(merged)

        # Get the middle point
        middle = len(merged) // 2

        # Return the median
        if len(merged) % 2 == 0: return (merged[middle] + merged[middle - 1]) / 2
        else: return merged[middle]
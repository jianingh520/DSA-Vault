class Solution:
    def unionArray(self, nums1, nums2):
        # put both nums1, nums2 into set, and sort it 
        # time O(n+m log n+m), space O(n+m)
        union = []
        n, m = len(nums1), len(nums2)
        i, j = 0, 0

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                if not union or union[-1] != num1[i]:
                    union.append(num1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                if not union or union[-1] != nums2[j]:                
                    union.append(nums2[j])
                j += 1
            else: # num1[i] ==  nums2[j]
                if not union or union[-1] != nums1[i]:
                    union.append(nums1[i])
                i += 1
                j += 1
            
        while i < n:
            if not union or union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1

        while j < m:
            if not union or union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1
        return union

        
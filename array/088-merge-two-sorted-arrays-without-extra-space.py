class Solution:
    def merge(self, nums1, m, nums2, n):
        # clarify: make sure both arr are sorted
        # naive: with extra sapce, iteratate through both nums1, nums2 with i, j pointers and compare them 
            # time O(m+n), auxilary space O(m+n) 
        # better: without extra space, merge from the back to avoid overwriting. 
            # interate through both nums1, nums2 from the back and start filling the result form the end of nums1. 
            # time O(m+n), auxilary space O(1)

        
        i, j = m-1, n-1
        k = m+n-1
        while i >=0 and j >=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # if any elements left in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -=1

        # no need to copy nums 1, already inplace
        # while i >= 0:
        #     nums1[k] = nums1[i]
        #     i -= 1
        #     k -= 1



class Solution:
	def findKthPositive(self, arr: List[int], k: int) -> int:
		"""
		# naive: linear search. Time O(n), Space O(1)
			core idea: if a number in the arr is sitting at
			 or below the current target k, then my real ans must
			 be pushed one step further
		"""
		# for num in arr:
		# 	if num <= k:
		# 		k += 1
		# 	else:
		# 		break
		# return k

		"""
		* optimized: binary search. Time O(logn), Space O(1)
		(Tricky) The answer we want is res + k, where res is 
		how many array numbers sit before the answer. 
		We do not know the answer directly, 
		but we know that the first index where missing >= k is exactly that count
		so we use binary search to find that index efficiently.

		"""
        l, r = 0, len(arr) -1
        res = len(arr)
        while l <= r:
            m = l + (r-l) // 2
            missing = arr[m] - (m+1)
            if missing >= k:
                res = m
                r = m -1
            else:
                l = m + 1
        return res + k
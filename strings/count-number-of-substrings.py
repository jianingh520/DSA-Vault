"""
Problem Statement: You are given a string s and a positive integer k.
Return the number of substrings that contain exactly k distinct characters.

Example 1:
	Input:
	 s = "pqpqs", k = 2  
	Output:
	 7  
	Explanation:
	  All substrings with exactly 2 distinct characters:  
	"pq", "pqp", "pqpq", "qp", "qpq", "pqs", "qs"  
	Total = 7.

"""

class Solution:
	def atMostKDistinct(self, s:str, k:int)-> int:
		"""
		use sliding window and a frequency map
		expand the window by moving the right pointer and count characters
		if count of distinct char exceeds k, shrink the window by moving the left pointer
		For each valid window, add (right - left + 1) to the result.

		To find substrings with exactly k distinct characters, calculate:
			atMostKDistinct(s, k) - atMostKDistinct(s, k-1)
		
		Time: O(n) for each call to atMostDistinct, Space: O(1) map size bounded by 26 characters for alphabets.
		"""

		l = 0
		freq = {}
		cnt = 0

		# expand the window
		for r in range(len(s)):
			freq[s[r]] = 1 + freq.get(s[r], 0)

			# shrinking if distinct char > k
			while len(freq) > k:
				freq[s[l]] -= 1
				if freq[s[l]] == 0:
					del freq[s[l]]
				l += 1

			# for each valid window, add (r-l+1) to the count
			cnt += (r - l + 1)

		return cnt

	def countSubstrings(self, s:str, k:int) -> int:
		return self.atMostKDistinct(s, k) - self.atMostKDistinct(s,k-1)






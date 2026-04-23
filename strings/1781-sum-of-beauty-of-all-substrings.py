"""
Problem Statement: The beauty of a string is defined as the difference between the frequency of the most frequent character and the least frequent character (excluding characters that do not appear) in that string.

Given a string s, return the sum of beauty values of all possible substrings of s.

"""


class Solution:
	def beautySum(self, s:str) -> int:
		"""
		naive: Extract each substring then build freq map
			Time O(n^3), Space O(n)
		better: loop through all substr of the sting, maintain a freq map of characters for each subtring
			for each substr, compute the beauty values and add to the res

			Time O(n^2) substings * O(26) for get min and max -> O(n^2)	
			Space O(1)
		"""
		res = 0
		n = len(s)
		for i in range(n):
			freq = {}
			for j in range(i, n):
				freq[s[j]] = 1 + freq.get(s[j], 0)
				beauty = max(freq.values()) - min(freq.values())
				res += beauty
		return res
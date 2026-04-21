"""
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.


"""

class Solution:
	def frequencySort(self, s: str) -> str:
		"""
		use hash map to store character frequency of s, then do bucket sort by putting char_key to corresponding freq bucket.
			get the result by iterate through the bucket list.
		Time: O(n), Space O(n)
		"""
		if not s:
			return s

		# store character frequency
		freq = {}
		for char in s:
			freq[char] = 1 + freq.get(char, 0)

		# bucket sort the char by freq
		max_freq = max(freq.values())
		buckets = [[] for _ in range(max_freq+1)]
		for c, f in freq.items():
			buckets[c].append(c)

		# build up the string
		res = []
		for i in range(len(buckets) -1, 0, -1):
			for c in buckets[i]:
				res.append(c*i)
		return "".join(res)
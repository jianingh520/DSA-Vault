"""
Problem Statement: Given two strings, check if two strings are anagrams of each other or not.

"""
class Solution:
	def isAnagram(self, s:str,t:str) -> bool:
		"""
		naive: generate every permutations of s, check if one of permutations == t.
			Time: O(N! * N),
			Space O(n)
		better: sort both stings and check if they are the same
			Time: O(nlogn), 
			Space O(n)
		opt: use hash map to store character frequencies of each string, and if all the key and value of each hash map are the same, then the two strings are anagrams.
			Time: O(n), 
			Space O(1) because the hash map stores at most 26 characters (a to z)
		"""
		if len(s) != len(t):
			return False

		freq = [0] * 26 
		for i in range(len(s)):
			freq[ord(s[i])-ord('a')] += 1
			freq[ord(t[i])-ord('a')] -= 1
		for f in freq:
			if f != 0:
				return False
		return True
		# return all(f == 0 for f in freq)  # every slot must be 0


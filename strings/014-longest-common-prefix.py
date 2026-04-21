"""
Write a function to find the longest common prefix string amongst an array of strings. 
If there is no common prefix, return an empty string "".

Example 1
Input:
 str = ["flower", "flow", "flight"]
Output:
 "fl"

Example 2
Input:
 str = ["apple", "banana", "grape", "mango"]
Output:
 ""


"""

class Solutions:
	def longestCommonPrefix(self, strs: list[str]) -> str:
		"""
		idea: The common prefix across all strings must exist between the smallest and largest string when sorted lexicographically.
		Time : O(N * log N + M), where N is the number of strings and M is the minimum length of a string. 
		Space: O(M) for output space, Auxiliary Space O(1)
		"""
		if not strs:
			return ""
		
		strs.sort()
		first = strs[0]
		last = strs[-1]
		res = []
		for i in range(min(len(first), len(last))):
			if first[i] != last[i]:
				return "".join(res)
			res.append(first[i])
		return "".join(res)

	def longestCommonPrefix_naive(self, strs: list[str]) -> str:
		"""
		naive: compare all strings character by character
		Time  O(n * m), Space O(m) for output, Auxiliary Space O(1)
		"""
		res = ""
		for i in range(len(strs[0])):      # go through each character position
		    for s in strs:                  # check every string at that position
		        if i == len(s) or s[i] != strs[0][i]:
		            return res
		    res += strs[0][i]
		return res
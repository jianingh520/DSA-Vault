"""
Problem Statement: Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

"""

class Solution():
	def maxDepth(self, s:str)-> int:
		"""
		track current depth by incrementing on "(" and decrementing on ")"
		update max depth after each "("
		return max depth at the end
		Time O(n), Space O(1)

		"""
		max_depth = 0
		depth = 0
		for char in s:
			if char == "(":
				depth += 1
				max_depth = max(depth, maxDepth)
			elif char == ")":
				depth -= 1 
		return max_depth

"""
Problem Statement: Given two strings s and goal, return true if 
	and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position. 
	For example, if s = "abcde", then it will be "bcdea" after one shift.

"""


class Solution:
	def rotateString_naive(self, s: str, goal: str) -> bool:
		"""
		naive: try all posible rotations of s, if rotation matches, return True, if no rotaion matches, return False.

		Time O(n^2), Space O(n)
		"""
		if len(s) != len(goal):
			return False

		# try all possible rotaions of s
		for i in range(len(s)):
			# generate a rotaion
			rotated = s[i:] + s[:i]
			if rotated == goal:
				return True

		return False

	def rotateString(self, s: str, goal: str) -> bool:
		"""
		better: double the original string by joining it with itself, creating a new string like s + s
			check if target string inside this new doubled string

		Time O(n). checking for a substring in s + s is linear in time.
		Space O(n). space for storing s+s
		"""
		if len(s) != len(goal):
			return False
			
		return goal in (s + s)
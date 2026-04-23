
"""
Problem Statement: 
Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
The number returned should not have leading zero's. But the given input string may have leading zero.

"""
class Solution:
	def largestOddNum(self, s:str)-> str:
		"""
		loop through from the end postion to find the first odd number. (would be the last odd in str)
		once the end position is determined, we identify the starting point by skipping any leading zeroes before it
		extract the portion between these two positions, this gives the largest possible odd integer from the string		
		Time O(n), Space O(1)
		"""
		ind = -1
		for i in range(len(s) -1 , -1, -1):
			if int(s[i]) % 2 ==1:
				ind = i
				break

		i = 0
		while s[i] == '0' and i < ind:
			i += 1

		return s[i: ind+1]

# driver code
solution = Solution()
num = "504"
result = solution.largestOddNum(num)
print("Largest odd number:", result)
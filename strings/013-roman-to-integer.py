"""
Problem Statement: Roman numerals are represented by seven different symbols: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
For example: 2 is written as II, 12 is written as XII, 27 is written as XXVII.
Roman numerals are usually written largest to smallest from left to right.
But in six special cases, subtraction is used instead of addition:

I before V or X → 4 and 9,
X before L or C → 40 and 90,
C before D or M → 400 and 900
Given a Roman numeral, convert it to an integer.




"""

class Solution:
    def romanToInt(self, s: str) -> int:
    	"""
		when smaller value appears before a larger one, it indicates subtraction instead of addition.
    	traverse the string, compare current string to the next string, 
    				if cur >= next, add cur to result
    				otherwise, subtract cur from result
    	add last character at the end since the loop stops before it
    	Time: O(n), Space O(1)				
    	
    	"""
    	roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    	res = 0
    	for i in range(len(s)-1):
    		if roman[s[i]] < roman[s[i+1]]:
    			res -= roman[s[i]]
    		else:
    			res += roman[s[i]]
    	return res + roman[s[-1]]


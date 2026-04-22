"""
Problem Statement: Implement the function myAtoi(s) which converts the given string 
	s to a 32-bit signed integer (similar to the C/C++ atoi function).

1. Whitespace: Ignore any leading whitespace (" ").
2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.


"""

class Solution:
	def myAtoi(self, s:str) -> int:
		"""
		follow the rule
		Time O(n), Space O(1)
		"""
		i = 0
		n = len(s)
		INT_MAX = 2**31 -1
		INT_MIN = -2**31 

		# skip leading zero
		while i < n and s[i] == ' ':
			i += 1

		# check for sign
		sign = 1
		if i < n and (s[i] == '-' or s[i] == '+'):
			if s[i] == '-':
                sign = -1
            i += 1

        # parse digits and build the number
        num = 0
        while i < n and ord('0') <= ord(s[i]) <= ord('9'):
        	digit = ord(s[i]) - ord('0')
        	num = num * 10 + digit
        	i += 1

        # apply sign
        num *= sign

        # clamp to 32 bit signed integer range
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num

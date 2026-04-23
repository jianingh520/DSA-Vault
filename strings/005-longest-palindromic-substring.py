"""

Given a string s, return the longest palindromic substring in s.

Example 1:

	Input: s = "babad"
	Output: "bab"
	Explanation: "aba" is also a valid answer.
Example 2:

	Input: s = "cbbd"
	Output: "bb"

"""



class Solution:
		"""
		naive: check all substrings, for each substrings, use two pointers to check if it is a palindrome and record its len
			Time: O(n^3) - O(n^2) substrings and for each substring check with O(n)
			Space O(1)

		dp: 
			Time O(n^2)
			Space O(n^2)

		expand from center: for each index, treat it as the center of a palindrome and expand outward 
				in both directions while the characters match.
				repeat for both odd length (single center) and even length (two character center).
			Time O(n^2)
			Space O(1)
		"""

    def expand(self, s: str, l: int, r: int):
        """
        expand outward from center while characters match
        return the start index and length of the longest palindrome found
        """
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # stopped one step too far, palindrome is between (l+1) and (r-1)
        length = r - l - 1
        start = l + 1
        return start, length

    def longestPalindrome(self, s: str) -> str:
        """
        expand from every possible center (odd and even)
        track the longest palindrome found
        Time: O(n^2), Space: O(1)
        """
        res_start, res_len = 0, 1  # at least one character

        for i in range(len(s)):
            # odd length: single character center
            start, length = self.expand(s, i, i)
            if length > res_len:
                res_len = length
                res_start = start

            # even length: two character center
            start, length = self.expand(s, i, i + 1)
            if length > res_len:
                res_len = length
                res_start = start

        return s[res_start: res_start + res_len]



class Solution:
	def isIsomorphic(self, s:str, t:str)-> bool:
		"""
 		Two strings are isomorphic if you can replace each character in s 
 		with another character to get t, and that mapping is consistent throughout.
		Time O(n), Auxiliary Space O(1)
		
		Every time character X appears in s, the SAME character Y 
			must appear in t at the exact same position.
		So if we track when each character last appeared, both characters 
			that are supposed to be paired must always show up at the same time.

		"""

        # Arrays to track last seen positions of characters
        m1, m2 = [0] * 256, [0] * 256
  
        # Get the length of the strings
        n = len(s)
  
        # Loop through each character in both strings
        for i in range(n):
            # Return False if last seen positions don't match
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False

            # Update last seen positions with current index + 1
            m1[ord(s[i])] = i + 1
            m2[ord(t[i])] = i + 1
  
        # Return True if no inconsistencies found
        return True
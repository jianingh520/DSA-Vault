"""
Problem Statement: 
Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space. 
Return a string with the words in reverse order, concatenated by a single space.

"""


class Solution:
	def reverseWords(self, s:str) -> str:
		"""
		naive: 1. split str by blank, traverse words from the right to left. create new s on the fly.
			Time: O(N), Space O(N), where N = number of characters in the string
			   2. split str by blank, use two pointer at the leftmost and rightmost postion, and swap word
			Time: O(N), Auxiliary Space O(N). split is O(n)

		better: traverse characters from right to left, extract words, build result.
    		Time: O(N), Auxiliary Space O(1), Space O(N) for result string

		"""
        result = ""
        i = len(s) - 1
        
        # traverse from right to left
        while i >= 0:
            # skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1
            
            # if pointer out of bounds, break
            if i < 0:
                break
            
            # mark end of word
            end = i
            
            # move left until space or start
            while i >= 0 and s[i] != " ":
                i -= 1
            
            # extract the word
            word = s[i + 1:end + 1]
            
            # add space if result is not empty
            if result != "":
                result += " "
            
            # append word
            result += word
        
        return result

if __name__ == "__main__":
    obj = Solution()
    s = " amazing coding skills "
    print(obj.reverseWords(s))

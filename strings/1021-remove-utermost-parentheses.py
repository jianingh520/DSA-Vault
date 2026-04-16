


class Solution:
    # function to remove outer parentheses
    def removeOuterParentheses(self, s):
        # initialize result string
        result = ""  
        # initialize nesting level counter
        level = 0     

        # traverse the string
        for char in s:
            # if we encounter '(', increase the level
            if char == '(':
                # if we're inside a primitive, add '(' to result
                if level > 0:
                    result += char
                # increase the nesting level for '('
                level += 1  
            elif char == ')':
                # decrease the nesting level for ')'
                level -= 1  
                # if we're inside a primitive, add ')' to result
                if level > 0:
                    result += char

        # return the final result after removing the outer parentheses
        return result

# example usage
s = "(()())(())"  
sol = Solution() 

print(sol.removeOuterParentheses(s)) 
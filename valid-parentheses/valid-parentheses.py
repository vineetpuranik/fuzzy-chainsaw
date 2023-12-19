from typing import List

class Solution:
    def isValid(self, s:str) -> bool:

        # if there is only a single character the string is invalid
        if len(s) == 1:
            return False


        # stack for storing all the opening brackets
        stack = []

        # sets for opening and closing brackets
        opening = set(['(', '{', '['])
        closing = set([')', '}', ']'])

        # mapping for opening and closing brackets
        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        for i in range(len(s)):

            # opening bracket is added to the top of the stack    
            if s[i] in opening:
                stack.append(s[i])

            # closing bracket
            else:

                # if stack does not have any characters then we return false sicne there is no opening 
                # bracket to match our closing bracket
                if len(stack) == 0:
                    return False    

                # pop the first item from the stack    
                pop = stack.pop()

                # if open and close brackets do not match
                if pop != mapping[s[i]]:
                    return False    


        # stack should be empty if we reach here which will indicate all the open brackets have
        # been mapped with the closed brackets
        if len(stack) == 0:
            return True
        else:
            return False    
# Brute force O(n^2) solution right now

class Solution:
    def countSubstrings(self, s: str) -> int:
        # constraints length is atleast 1 

        # declare result variable
        result = 0 

        # we need to list all the substrings in the string
        # post that we need to identify the number of palindromes from the substrings. 

        substrings = []    
        # gather all the substrings for the input string
        def gather(input):
            # add all the possible substrings
            for i in range(len(input)):
                substrings.append(input[i])
                for j in range(i-1, -1, -1):
                    substrings.append(input[j:i+1])
        
        # check if input string is a palindrome
        def isPalindrome(input):
            # single character string is always a palindrome
            if len(input) == 1:
                return True
            left, right = 0, len(input) - 1
            while left < right : 
                if input[left] != input[right]:
                    return False
                left += 1
                right -= 1
            return True

        # gather all substrings        
        gather(s)

        for substring in substrings:
            if isPalindrome(substring):
                result += 1
        
        return result



        

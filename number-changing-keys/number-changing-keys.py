# you are given a 0 indexed string s typed by a user. 
# Changing a key is defined as using a key different from the last used key
# s = "ab" number of keys changes = 1
# s = "bBBb" number of key changes = 0 

# s = "aAbBcC"
# change = 0 ; last = a 
# change = 0 ; last = A 
# change = 1; last b
# change = 1 ; last B
# change = 2 ; last c


# key is to use the s.lower() function in python

class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if s is length 1 then return 0 
        if len(s) == 1 :
            return 0

        # convert s to lower case
        s_lower = s.lower()
        last = s_lower[0]
        change = 0

        # start checking from the 2nd character
        for i in range(1, len(s_lower)):
            current = s_lower[i]
            if current != last:
                change += 1
            last = current    

        return change



        
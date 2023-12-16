class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 string are anagrams if each other if they have the same length and contain the same letters in the same order of different order
        
        # s and t are 2 input strings
        # s and t are non null strings
        
        # if s and t are of different lengths, then they are definitely not anagrams of each other
        
        if len(s) != len(t):
            return False
        
        # create 2 hash maps for both s and t
        # key will be the letters and value will be the number of times a letter occurs
        smap = {}
        tmap = {}
        
        # since s and t are of the same length we can populate smap and tmap using 1 for loop
        for i in range(len(s)):
            smap[s[i]] = 1 + smap.get(s[i], 0) # if s[i] does not exist then return 0 to avoid key not found error
            tmap[t[i]] = 1 + tmap.get(t[i], 0)
        
        # if both smap and tmap are the same exact maps then both s and t are anagrams of each other
        # else they are not anagrams of each other
        
        for k in smap:
            if (k not in tmap) or (k in tmap and smap[k] != tmap[k]):
                return False
        
        
        return True
    
    # time complexity : O(s + t), O(s + t) = O(s + t)
    # space complexity : O(2(s + t)) = O(s + t)

    # We can also sort the 2 strings and then check if they are exactly same. O(nlogn) and O(1) solution
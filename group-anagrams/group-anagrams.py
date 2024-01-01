class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strings eat and ate are anagrams of each other

        # one way is to sort all the input strings.
        # anagram strings will be equal to each other after sorting
        # this will take Omnlogn time

        # alternate way
        # for each string count frequencies of a - z
        # that will be the key to our hashmap


        result = defaultdict(list) # mapping charCount to list of anagrams

        for s in strs:
            # initialize count as a list of 26 indices
            # the value at each index will be initially 0 
            # index 0 corresponds to a
            # index 25 corresponds to z
            # az = [1...........1] => 0th and 25th index will have the count as 1
            count = [0] * 26 

            # iterate each character in the string
            for c in s: 
                count[ord(c) - ord("a")] += 1
                # ascii of character - ascii of a will give the index of the 
                # current character in count

            # add count to hashmap
            # cannot directly add count to hashMap hence we convert it to a tuple to add
            result[tuple(count)].append(s)
        

        return result.values()

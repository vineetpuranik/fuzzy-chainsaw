# add and search words
# we will be using a Trie data structure


# TrieNode
# chars is a dictionary where the keys are the characters that originate from the current node and the values are the TrieNodes for those characters
class TrieNode:
    def __init__(self):
        self.chars = {}
        self.isTerminal = False

class WordDictionary:
    # create the root node
    def __init__(self):
        self.root = TrieNode()    

    # add word is similar to the Trie implementation
    def addWord(self, word: str) -> None:
        # start from the root of the Trie
        current = self.root
        
        for char in word:
            if char not in current.chars:
                current.chars[char] = TrieNode()
            current =  current.chars[char]

        current.isTerminal = True

        return    

    # search will be recursive in this case since we have to deal with dots
    def search(self, word: str) -> bool:

        def dfs(j, root):
            current = root
            for i in range(j, len(word)):
                # current character that we are considering
                char = word[i]
                # current character is a dot then we have to possibly navigate all the children referred in the chars dictionary for the current node
                if char == '.':
                    # we need to check all the children for the current node
                    # value is the TrieNode hence we have chars.values()
                    for child in current.chars.values():
                        # we want to do recursion here which will start from the i + 1 character since the ith character is a dot
                        if dfs(i + 1, child):
                            # if any of the recursive calls return True then we will return True and stop the recursion
                            return True
                    # all paths tested so return False
                    return False

                # current character is not a dot
                # regular check        
                else:
                    if char not in current.chars:
                        return False
                    current = current.chars[char]

            # if we reach here that means the last character was not a dot
            return current.isTerminal

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

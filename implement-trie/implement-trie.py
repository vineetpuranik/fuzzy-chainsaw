class TrieNode:

    def __init__(self):
        self.children = {}
        self.isTerminal = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #start with root
        current = self.root

        #iterate each character in input word    
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
                
        current.isTerminal = True        

        

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]

        return current.isTerminal
            
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]

        return True    
        
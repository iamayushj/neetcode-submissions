class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children: 
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.is_end = True       

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i in curr.children:
                curr = curr.children[i]
            else:
                return False
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if i in curr.children:
                curr = curr.children[i]
            else:
                return False
        return True
        
class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(root, index):
            curr = root
            for ch in range(index, len(word)):
                i = word[ch]
                if i == ".":
                   for child in curr.children.values():
                    if (dfs(child, ch + 1)):
                        return True
                   return False 
                else:
                    if i not in curr.children:
                        return False    
                    curr = curr.children[i]
            return curr.is_end
        return dfs(self.root, 0)


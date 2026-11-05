class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_eow = True

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)
        
    def _dfs(self, word: str, idx: int, node: TrieNode) -> bool:
        if idx == len(word):
            return node.is_eow
        
        c = word[idx]
        if c == '.':
            for child in node.children.values():
                if self._dfs(word, idx+1, child):
                    return True
            return False
        
        if c not in node.children:
            return False
        
        return self._dfs(word, idx+1, node.children[c])
            

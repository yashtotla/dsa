class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_eow = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = PrefixTree()
        for word in words:
            trie.insert(word)
        
        rows, cols = len(board), len(board[0])
        ans = set()

        for r in range(rows):
            for c in range(cols):
                self._dfs(board, r, c, trie.root, "", ans)
        
        return list(ans)
    
    def _dfs(self, board, r, c, node, path, ans):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return
        
        ch = board[r][c]

        if ch == "-1" or ch not in node.children:
            return
        
        node = node.children[ch]
        path += ch
        if node.is_eow:
            ans.add(path)

        board[r][c] = "-1"

        self._dfs(board, r + 1, c, node, path, ans)
        self._dfs(board, r - 1, c, node, path, ans)
        self._dfs(board, r, c + 1, node, path, ans)
        self._dfs(board, r, c - 1, node, path, ans)

        board[r][c] = ch


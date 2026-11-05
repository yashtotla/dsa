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
        ans = []

        for r in range(rows):
            for c in range(cols):
                self._dfs(board, r, c, trie.root, "", ans)
        
        return ans
    
    def _dfs(self, board, r, c, parent, path, ans):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            return
        
        ch = board[r][c]

        if ch == "-1" or ch not in parent.children:
            return
        
        node = parent.children[ch]
        path += ch
        if node.is_eow:
            ans.append(path)
            node.is_eow = False

        board[r][c] = "-1"

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            self._dfs(board, r+dr, c+dc, node, path, ans)

        board[r][c] = ch

        if not node.children:
            del parent.children[ch]


class Solution:
    def _dfs(self, heights, prev_height, r, c, ocean):
        if r<0 or r>=len(heights) or c<0 or c>=len(heights[0]):
            return
        if ocean[r][c] == 1:
            return
        if heights[r][c] < prev_height:
            return
        
        ocean[r][c] = 1
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            self._dfs(heights, heights[r][c], r+dr, c+dc, ocean)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pacific = [[0] * col for _ in range(row)]
        atlantic = [[0] * col for _ in range(row)]

        for r in range(row):
            self._dfs(heights, 0, r, 0, pacific)
            self._dfs(heights, 0, r, col-1, atlantic)
        
        for c in range(col):
            self._dfs(heights, 0, 0, c, pacific)
            self._dfs(heights, 0, row-1, c, atlantic)
        
        ans = []
        for r in range(row):
            for c in range(col):
                if pacific[r][c] == 1 and atlantic[r][c] == 1:
                    ans.append([r,c])
        
        return ans

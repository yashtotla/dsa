class Solution:
    DIR = [(-1,0),(1,0),(0,-1),(0,1)]

    def _dfs(self, grid, r, c):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
            return
        if grid[r][c] == "0":
            return

        grid[r][c] = "0"
        
        for dr, dc in self.DIR:
            self._dfs(grid, r+dr, c+dc)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0":
                    continue
                self._dfs(grid, r, c)
                islands += 1
        return islands

class Solution:
    def _dfs(self, grid, r, c):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
            return
        if grid[r][c] == 1:
            return
        grid[r][c] = 1
        stack = [(r,c)]

        while stack:
            cr,cc = stack.pop()
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = cr+dr, cc+dc
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==0:
                    grid[nr][nc] = 1
                    stack.append((nr,nc))

    def closedIsland(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        
        ## O(row x col)
        for r in range(row):
            self._dfs(grid, r, 0)
            self._dfs(grid, r, col-1)
        
        ## O(col x row)
        for c in range(col):
            self._dfs(grid, 0, c)
            self._dfs(grid, row-1, c)
        
        count = 0
        
        ## O(row x col)
        for r in range(1,row-1):
            for c in range(1,col-1):
                if grid[r][c] == 1:
                    continue
                count += 1
                self._dfs(grid, r, c)
        
        return count

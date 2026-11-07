from collections import deque

class Solution:
    DIR = [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(1,1),(-1,1),(-1,-1)]

    def _isValidIndex(self, r, c, row, col):
        if r<0 or c<0 or r>=row or c>=col:
            return False
        return True

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return -1
        if row==1 and col==1:
            return 1
        
        q = deque()
        q.append((0,0,1))
        grid[0][0] = 1

        while q:
            r,c,dist = q.popleft()
            for dr,dc in self.DIR:
                if self._isValidIndex(r+dr,c+dc,row,col):
                    if r+dr == row-1 and c+dc == col-1:
                        return dist+1
                    if grid[r+dr][c+dc] == 0:
                        grid[r+dr][c+dc] = 1
                        q.append((r+dr,c+dc,dist+1))
        
        return -1

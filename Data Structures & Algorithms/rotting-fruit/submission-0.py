class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = collections.deque()
        fresh  = 0
        row_count = len(grid)
        col_count = len(grid[0])

        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == 2:
                    rotten.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minute = 1
        while rotten:
            qlen = len(rotten)
            for _ in range(qlen):
                r, c = rotten.popleft()
                if (r+1) < row_count and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    rotten.append([r+1, c])
                    fresh -= 1

                if (r-1) >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    rotten.append([r-1, c])
                    fresh -= 1

                if (c+1) < col_count and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    rotten.append([r, c+1])
                    fresh -= 1
                
                if (c-1) >= 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    rotten.append([r, c-1])
                    fresh -= 1

            if fresh <= 0:
                return minute
            minute += 1
        
        return -1

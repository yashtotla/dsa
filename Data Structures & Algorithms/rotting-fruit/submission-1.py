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

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minute = 1

        while rotten:
            qlen = len(rotten)
            for _ in range(qlen):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < row_count
                        and 0 <= nc < col_count
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        rotten.append((nr, nc))

            if fresh <= 0:
                return minute
            minute += 1
        
        return -1

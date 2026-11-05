class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_col = [row[0] for row in matrix]
        l, r = 0, len(first_col) - 1
        while l <= r:
            m = int(l + (r-l)/2)
            if first_col[m] == target:
                return True
            if first_col[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        row = matrix[l-1]
        l, r = 0, len(row) - 1
        while l <= r:
            m = int(l + (r-l)/2)
            if row[m] == target:
                return True
            if row[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
        
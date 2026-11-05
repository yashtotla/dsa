class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col - 1
        while l <= r:
            m = l + (r-l)//2
            val = matrix[m // col][m % col]
            if val == target:
                return True
            if val > target:
                r = m - 1
            else:
                l = m + 1
        return False

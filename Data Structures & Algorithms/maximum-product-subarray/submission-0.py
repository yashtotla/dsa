class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_min, curr_max = 1, 1
        for n in nums:
            if n == 0:
                res = max(res, 0)
                curr_min, curr_max = 1, 1
                continue
            t = curr_max * n
            curr_max = max(t, n * curr_min, n)
            curr_min = min(t, n * curr_min, n)
            res = max(res, curr_max)
        return res
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        s = set(nums)
        for n in nums:
            if n-1 in s:
                continue
            cur_len = 0
            cur_n = n
            while cur_n in s:
                cur_len += 1
                cur_n += 1
            max_len = max(max_len, cur_len)
        return max_len
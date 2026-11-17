class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        prev_two = nums[0]
        prev_one = max(nums[0],nums[1])
        ans = max(prev_two,prev_one)

        for i in range(2, len(nums)):
            curr = max(prev_two + nums[i], prev_one)
            ans = max(curr, ans)
            prev_two = prev_one
            prev_one = curr
        
        return ans
